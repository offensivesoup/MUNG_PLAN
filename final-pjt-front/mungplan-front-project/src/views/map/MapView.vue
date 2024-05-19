<template>
  <header class="header">
    <button @click="getPlace('서비스')" id="select-btn" type="button">서비스</button>
    <button @click="getPlace('의료')" id="select-btn" type="button">의료</button>
    <button @click="getPlace('식당')" id="select-btn" type="button">식당 카페</button>
    <button @click="getPlace('여행')" id="select-btn" type="button">문화 여행</button>
  </header>

  <main class="main">
    <naver-map ref="map" class="map" :map-options="mapOptions" @onLoad="onLoadMap($event)"  @idle="onIdle"></naver-map>
    <naver-marker v-for="place in placeList" 
    :key=place.id 
    :latitude="Number(place.facility_lat)" 
    :longitude="Number(place.facility_lng)"
    @onLoad="onLoadMarker($event)" 
    @click="selectMarker(place)">
    <div class="marker-place">
      <img class="marker" src="@/assets/dog_foot.png" alt="">
    </div>
  </naver-marker>
    <naver-info-window :open="isOpen" :marker="targetMarker" @onLoad="onLoadInfoWindow($event)">
      <div v-if="targetPlace" id="info-place">
        장소 : {{ targetPlace.facility_name }} <hr>
        위치 : {{ targetPlace.facility_new_address }} <hr>
        주차 : {{ targetPlace.facility_parking }} <hr>
        <p v-if="targetPlace.facility_link !=='정보없음'">
        링크 : <a :href=targetPlace.facility_link>바로가기</a> <hr>
        </p>
        <p v-else>
        링크 : 정보 없음 <hr>  
        </p>
      </div>
    </naver-info-window>
    <p v-if="errorMessage">{{ errorMessage }}</p>
  </main>
</template>


<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue'
import { NaverMap, NaverMarker , NaverInfoWindow } from 'vue3-naver-maps'
import { useMapStore } from '@/stores/map'

const store = useMapStore()

// 지도의 출력과 관련된 부분

const latitude = ref(37.51347)
const longitude = ref(127.041722)
const errorMessage = ref(null)
const map = ref()
const mapOptions = ref({})
const markerLatitude = ref(latitude.value)
const markerLongitude = ref(longitude.value)
const mapData = ref(null)
const infoWindow = ref()

const onLoadMap = (mapObject) => {
  map.value = mapObject
  mapData.value = mapObject
}

const onIdle = () => {
  if (map.value) {
    map.value = mapData.value
    const center = map.value.getCenter()
    console.log(center)
    markerLatitude.value = center.lat()
    markerLongitude.value = center.lng()
  }
}

const getLocation = () => {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        latitude.value = position.coords.latitude;
        markerLatitude.value = position.coords.latitude;
        longitude.value = position.coords.longitude;
        markerLongitude.value = position.coords.longitude;
        updateMap();
      },
      (error) => {
        switch (error.code) {
          case error.PERMISSION_DENIED:
            errorMessage.value = "사용자가 위치 권한을 거부하였습니다.";
            break;
          case error.POSITION_UNAVAILABLE:
            errorMessage.value = "위치 정보를 사용할 수 없습니다.";
            break;
          case error.TIMEOUT:
            errorMessage.value = "위치 정보를 사용할 수 없습니다.";
            break;
          case error.UNKNOWN_ERROR:
            errorMessage.value = "위치 정보를 사용할 수 없습니다.";
            break;
        }
      }
    );
  } else {
    errorMessage.value = "위치 정보를 사용할 수 없습니다.";
  }
};

const updateMap = () => {
  mapOptions.value = {
    ...mapOptions.value,
    center: { lat: markerLatitude.value, lng: markerLongitude.value },
    zoom: 12,
    zoomControl: false,
  }
}

onMounted(() => {
  getLocation()
})

// 지도의 마커와 관련

const placeList = ref([])
const markers = ref([])
const targetMarker = ref()
const targetPlace = ref()
const isOpen = ref(false)

const onLoadMarker = (markerObject) => {
  markers.value.push(markerObject);
};

const getPlace = (word) => {
  placeList.value = []
  axios({
    method : 'GET',
    url : `${store.API_URL}/maps/${word}/${markerLatitude.value}/${markerLongitude.value}`
  })
    .then((response) => {
      if (response.data.length === 0) {
        console.log('결과가 없음')
        updateMap();
      } else {
      console.log(response.data)
      placeList.value = response.data.filter(place => place.facility_lat && place.facility_lng)
      updateMap();
      }
    })
    .catch((error) => {
       console.log(error)
     })
}

const onLoadInfoWindow = (infoWindowObject) => {
  infoWindow.value = infoWindowObject
}

// 해당 마커를 클릭했을 때 나오는 정보 리스트와 관련
const selectMarker = (place) => {
  // 해당 마커를 중심으로 지도 이동
  targetPlace.value = []
  map.value = mapData.value
  isOpen.value = !isOpen.value
  const coord = { lat: Number(place.facility_lat), lng: Number(place.facility_lng)}
  map.value.morph(coord,15)
  markers.value.forEach((marker) => {
    if (marker.position.y === coord.lat && marker.position.x === coord.lng) {
      targetMarker.value = marker
      targetPlace.value = place
      console.log(targetPlace.value)
    }
  }
  )
}

</script>


<style scoped>
  .main {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 100vh; /* Ensure the main container takes full viewport height */
  }

  .map {
    width: 100%;
    height: 100%; /* Ensure the map takes full height of its container */
  }

  .header {
    position: fixed;
    top: 100px;
    left: 17%;
    transform: translateX(-50%);
    display: flex;
    gap: 10px; /* Ensure there is a 10px gap between buttons */
    z-index: 1000; /* Ensure the header is above the map */
  }

  #select-btn {
    background-color: white;
    color: black;
    border-color: whitesmoke;
    border-radius: 35%;
    padding:5px 10px;
  }

  #info-place {
    position : absolute;
    bottom:0px;
    right:-50px;
    text-align: center;
    background-color: white;
    padding: 10px;
    width : 100px;
    height : 250px;
    font-size : 10px;
    border: black solid 2px;
    border-radius: 30px;
  }

  .marker {
    position:absolute;
    top:22px;
    right:-10px;
    width:20px;
    border-radius: 50px;
  }

</style>

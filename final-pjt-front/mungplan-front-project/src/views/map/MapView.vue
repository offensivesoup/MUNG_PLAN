<template>
    <div class="container">
      <div class="accordion" id="map-accordion">
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
              Accordion Item #1
            </button>
          </h2>
          <div id="collapseOne" class="accordion-collapse collapse show" data-bs-parent="#map-accordion">
            <div class="accordion-body">
              <strong>This is the first item's accordion body.</strong> It is shown by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
            </div>
          </div>
        </div>
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
              Accordion Item #2
            </button>
          </h2>
          <div id="collapseTwo" class="accordion-collapse collapse" data-bs-parent="#map-accordion">
            <div class="accordion-body">
              <strong>This is the second item's accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
            </div>
          </div>
        </div>
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
              Accordion Item #3
            </button>
          </h2>
          <div id="collapseThree" class="accordion-collapse collapse" data-bs-parent="#map-accordion">
            <div class="accordion-body">
              <strong>This is the third item's accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
            </div>
          </div>
        </div>
      </div>
      <main class="main">
        <h1 class="title">강아지도 갈 수 있다</h1>
        <naver-map ref="map" class="map" :map-options="mapOptions"></naver-map>
        <p v-if="errorMessage">{{ errorMessage }}</p>
      </main>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { NaverMap } from 'vue3-naver-maps'
  
  const latitude = ref(37.51347)
  const longitude = ref(127.041722)
  const errorMessage = ref(null)
  
  const getLocation = () => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          latitude.value = position.coords.latitude
          longitude.value = position.coords.longitude
          updateMap()
        },
        (error) => {
          switch (error.code) {
            case error.PERMISSION_DENIED:
              errorMessage.value = "사용자가 위치 권한을 거부하였습니다."
              break
            case error.POSITION_UNAVAILABLE:
              errorMessage.value = "위치 정보를 사용할 수 없습니다."
              break
            case error.TIMEOUT:
              errorMessage.value = "위치 정보를 사용할 수 없습니다."
              break
            case error.UNKNOWN_ERROR:
              errorMessage.value = "위치 정보를 사용할 수 없습니다."
              break
          }
        }
      )
    } else {
      errorMessage.value = "위치 정보를 사용할 수 없습니다."
    }
  }
  
  const mapOptions = ref({
    latitude: latitude.value,
    longitude: longitude.value,
    zoom: 12,
    zoomControlOptions: { position: "TOP_RIGHT" },
  })
  
  const updateMap = () => {
    mapOptions.value = {
      ...mapOptions.value,
      latitude: latitude.value,
      longitude: longitude.value,
    }
  }
  
  onMounted(() => {
    getLocation()
  })
  </script>
  
  <style scoped>
    .container {
    display: flex;
    height: 100vh;
    justify-content: space-between; /* Optional: adjust as needed */
    }

    #map-accordion {
    width: 30%;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    justify-content: center; /* Center vertically */
    }
  
  .main {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 70%;
  }
  
  .map {
    width: 100%;
    height: 100%;
  }
  
  .title {
    margin-bottom: 20px;
  }
  </style>
  
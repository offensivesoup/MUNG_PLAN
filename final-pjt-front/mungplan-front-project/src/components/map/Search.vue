<template>
  <div class="form-container">
    <label for="province-select">이동하실 지역을 선택해주세요</label>
    <select id="province-select" v-model="selectedRegion" @change="onRegionChange">
      <option value="" disabled>선택하세요</option>
      <option v-for="region in regions" :key="region" :value="region">{{ region }}</option>
    </select>
    <p>선택된 지역: {{ selectedRegion }}</p>
    <button @click="submitLocation(selectedRegion)">이동하기</button>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, defineProps, defineEmits } from 'vue';
import { useMapStore } from '@/stores/map'
const store = useMapStore()
const lat = ref()
const lng = ref()

const emits = defineEmits(['locationSelected'])

// 8도 및 주요 광역시 리스트
const regions = ref([
  '서울특별시',
  '부산광역시',
  '대구광역시',
  '인천광역시',
  '광주광역시',
  '대전광역시',
  '울산광역시',
  '세종특별자치시',
  '강원도',
  '경기도',
  '경상남도',
  '경상북도',
  '전라남도',
  '전라북도',
  '충청남도',
  '충청북도'
]);

const selectedRegion = ref('');

// 선택된 지역이 변경되었을 때의 핸들러 함수
const onRegionChange = () => {
  console.log(`선택된 지역: ${selectedRegion.value}`);
};

const submitLocation = function (region) {
  axios({
    method: 'GET',
    url: `${store.API_URL}maps/${region}/`
  })
    .then(response => {
      lat.value = response.data.latitude
      lng.value = response.data.longitude
      emits('locationSelected', lat.value, lng.value)
    })
    .catch(error => {
      console.log(error)
    })
}

</script>

<style scoped>
.form-container {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 50px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  max-width: 1700px;
}

label {
  font-weight: bold;
}

select {
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

p {
  font-size: 16px;
  color: #333;
}
</style>

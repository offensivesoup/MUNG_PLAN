<template>
  <div class="adopt-list-item">
    <div class="card col-lg-4 col-md-6">
      <img class="dog-image card-img-top" :src="dog.img" alt="shelterDog">
      <div class="card-body">
        <p class="card-text">{{ dog.state }}</p>
        <p class="card-title">{{ dog.kind.replace('[개]', '') }}</p>
        <p class="card-text">{{ dog.gender === 'F' ? '여성' : dog.gender === 'M' ? '남성' : '중성화 완료' }}</p>
        <p class="card-text">{{ dog.center_address.split(' ').slice(0, 2).join(' ') }}</p>
        <button type="button" class="btn btn-primary" :data-bs-toggle="'modal'" :data-bs-target="'#modal-' + dog.id">
          알아보기
        </button>
      </div>
    </div>

    <!-- Modal -->
    <div class="modal fade" :id="'modal-' + dog.id" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1"
      :aria-labelledby="'modalLabel-' + dog.id" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <img class="dog-modal-image card-img-top" :src="dog.img" alt="shelterDog">
          </div>
          <div class="modal-body">
            <p>현재: {{ dog.state }}</p>
            <p>보호 시작 일자: {{ dog.start_date }}</p>
            <p>보호 종료 일자: {{ dog.end_date }}</p>
            <p>특징: {{ dog.notice }}</p>
            <p>성별: {{ dog.gender === 'F' ? '여성' : dog.gender === 'M' ? '남성' : '중성화 완료' }}</p>
            <p>종: {{ dog.kind.replace('[개]', '') }}</p>
            <p>위치: {{ dog.center_address }}</p>
            <p>전화: {{ dog.center_telephone }}</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn" data-bs-dismiss="modal">돌아가기</button>
            <a :href="centerLink" target="_blank"><button type="button" class="btn">보호소 보기</button></a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  dog: Object
})

const centerLink = computed(() => `http://search.naver.com/search.naver?query=${props.dog.center_name}`)

</script>

<style scoped>
.adopt-list-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 20px;
  /* box-sizing: content-box; */
}

.card {
  width: 80%;
  height: 26rem;
  /* 세로 길이를 조정합니다. */
  border-radius: 25px;
  /* 테두리를 둥글게 만듭니다. */
  overflow: hidden;
  /* 둥근 테두리 내부의 내용이 넘치지 않도록 합니다. */
  border: 0;
  margin-bottom: 30px;
  background-color: rgb(253, 251, 237);
  box-shadow: 0 2px 6px;
  transition: transform 0.8s ease, box-shadow 0.8s ease;
}

.card:hover {
  transform: translateY(-30px);
  /* 마우스가 올라갔을 때 카드를 위로 10px 이동시킵니다. */
  box-shadow: 0 4px 12px;
  /* 마우스가 올라갔을 때 그림자를 더 크게 만듭니다. */
  z-index: 1;
}

.dog-image {
  height: 200px;
  background-size: cover;
  /* 이미지를 가능한 한 크게 확장하되, 이미지의 일부가 잘릴 수 있게 하려면 cover를 사용 */
  background-position: center;
  padding: 20px;
  border-radius: 50px;
  /* 이미지를 중앙에 위치시키려면 center를 사용 */
  /* object-fit: cover; */
}

.card-body {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1rem;
  font-size: 1rem;
  font-weight: bolder;
  color: #333;

}

.card-text {
  margin-bottom: 0.5rem;
}

.btn-primary {
  margin-top: 1rem;
  background-color: rgb(252, 226, 194, 0.3);
  border: none;
  color: black;
  font-weight: bold;
}

.btn-primary:focus {
  outline: 0;
}

.btn-primary:hover {
  background-color: rgb(252, 226, 194, 0.9);
  cursor: pointer;
}


.modal-content {
  z-index: 1050 !important;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 10%;
}

.dog-modal-image {
  width: 300px;
  height: 300px;
  border-radius: 30%;
  margin: 20px;
}
</style>
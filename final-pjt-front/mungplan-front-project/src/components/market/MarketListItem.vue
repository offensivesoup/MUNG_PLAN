<template>
  <div class="market-list-item">
    <div class="card" style="width: 18rem;">
      <img class="product-image card-img-top" :src="product.item_img" alt="product">
      <div class="card-body">
        <p class="card-text" v-html="product.item_name"></p> <!-- v-html 디렉티브를 사용하여 HTML 문자열을 렌더링 -->
        <p class="card-text">{{ product.item_low_price }}원</p>
        <a :href="generatedUrl" class="btn btn-primary" target="_blank"> 상세보기</a>
        <!-- target="_blank" 속성을 사용하여 새 창에서 링크 열기 -->
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, defineProps } from 'vue'

// 상품 상제 url 올바르게 생성
const props = defineProps({
  product: {
    type: Object,
    default: () => ({ item_name: '', }) // 기본값 설정
  }
})
console.log(props)

const extractKeywords = (htmlString) => {
  const strippedHtml = htmlString.replace(/<[^>]*>?/gm, '') // HTML 태그 제거
  const words = strippedHtml.split(' ') // 띄어쓰기 단위로 분리
  return words.join('+') // '+'로 연결하여 쿼리 문자열 생성
}

const query = computed(() => extractKeywords(props.product.item_name));

const generateUrl = (query) => {
  return `https://search.shopping.naver.com/search/all?query=${query}`
}

const generatedUrl = computed(() => generateUrl(query.value))
</script>

<style scoped>
.market-list-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 20px;
}

.card {
  width: 80%;
  height: 26rem;
  min-height: 30rem;
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

.product-image {
  height: 200px;
  background-size: cover;
  /* 이미지를 가능한 한 크게 확장하되, 이미지의 일부가 잘릴 수 있게 하려면 cover를 사용 */
  background-position: center;
  padding: 20px;
  border-radius: 50px;
  /* 이미지를 중앙에 위치시키려면 center를 사용 */
}

.card-body {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1rem;
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
</style>
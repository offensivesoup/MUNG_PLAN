<template>
  <div class="market-list-item">
    <div class="card" style="width: 18rem;">
      <img class="product-image card-img-top" :src="product.item_img" alt="product">
      <div class="card-body">
        <p class="card-text" v-html="product.item_name"></p> <!-- v-html 디렉티브를 사용하여 HTML 문자열을 렌더링 -->
        <p class="card-text">{{ product.item_low_price }}원</p>
        <a :href="generatedUrl" class="btn btn-primary" target="_blank"> 상세보기</a> <!-- target="_blank" 속성을 사용하여 새 창에서 링크 열기 -->   
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
    default: () => ({ item_name: '' }) // 기본값 설정
  }
})

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
    width: 100%;
  }

  .product-image {
    height: 200px;
    background-size: cover; /* 이미지를 가능한 한 크게 확장하되, 이미지의 일부가 잘릴 수 있게 하려면 cover를 사용 */
    background-position: center; /* 이미지를 중앙에 위치시키려면 center를 사용 */
    /* object-fit: cover; */
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
  }
</style>
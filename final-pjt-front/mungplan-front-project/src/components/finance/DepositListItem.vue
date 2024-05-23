<template>
  <div class="deposit-list-item">
    <div class="card card-parent">
      <div class="card-body">
        <!-- <div class="content" style="flex: 7;">
          <div class="card-logo-and-title">
            <img class="company-image" :src="`${depositStore.API_URL}${depositStore.staticUrl}${deposit.company_image}`"
              alt="company logo">
            <div class="card-titles">
              <h5 class="card-title">{{ deposit.product_name }}</h5>
              <h6 class="card-subtitle mb-2 text-muted">{{ deposit.company_name }}</h6>
            </div>
          </div>
          <p class="card-text"> 최고 금리: {{ deposit.maxi_interate_rate }}%</p>
          <p class="card-text"> 기본 금리: {{ deposit.interate_rate }}%</p>
        </div> -->
        <div class="card mb-3" style="max-width: 540px; padding-top: 30px;">
          <div class="row g-0">
            <div class="col-md-4" style="padding: 20px 0px 0px 20px">
              <img class="company-image img-fluid rounded-start"
                :src="`${depositStore.API_URL}${depositStore.staticUrl}${deposit.company_image}`" alt="company logo">
            </div>
            <div class="col-md-8">
              <div class="card-body" style="height: 100px; padding-left: 3px;">
                <h5 class="card-title">{{ deposit.product_name.split('(')[0].trim() }}</h5>
                <h6 class="card-subtitle mb-2 text-muted">{{ deposit.company_name }}</h6>
                <p class="card-text"> 최고 금리: {{ deposit.maxi_interate_rate }}%</p>
                <p class="card-text"> 기본 금리: {{ deposit.interate_rate }}%</p>
              </div>
            </div>
          </div>
        </div>
        <div class="card-actions" style="flex: 3;">
          <button type="button" class="btn btn-primary" :data-bs-toggle="'modal'"
            :data-bs-target="'#modal-' + deposit.id">
            알아보기
          </button>
          <button @click="toggleLike" class="btn btn-primary">
            {{ liked ? 'Unlike' : 'Like' }}
          </button>
        </div>
      </div>
    </div>
    <!-- Modal -->
    <div class="modal fade" :id="'modal-' + deposit.id" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1"
      :aria-labelledby="'modalLabel-' + deposit.id" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <img class="bank-modal-image card-img-top"
              :src="`${depositStore.API_URL}${depositStore.staticUrl}${deposit.company_image}`" alt="없음">
          </div>
          <div class="modal-body">
            <p>회사명: {{ deposit.company_name }}</p>
            <p>상품명: {{ deposit.product_name }}</p>
            <p>카테고리 : {{ deposit.category }}</p>
            <p>가입조건 : {{ deposit.join_member }}</p>
            <div v-if="deposit.limit">
              <p>가입상한액 : {{ deposit.limit }}</p>
            </div>
            <div v-else>
              <p>가입상한액: 없음</p>
            </div>
            <p>부가 조건 : {{ deposit.special_explain }}</p>
            <p>관심 수: {{ deposit.like_users.length }}개</p>

          </div>
          <div class="modal-footer">
            <button type="button" class="btn" data-bs-dismiss="modal">돌아가기</button>
            <a :href="deposit.link" target="_blank"><button type="button" class="btn">은행 보기</button></a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { ref } from 'vue'
import axios from 'axios'
import { useDepositStore } from '@/stores/deposit'
import { useAccountStore } from '@/stores/account'
import Swal from 'sweetalert2'
import { useRouter } from 'vue-router'
// import router from '../../router'

const router = useRouter()
const props = defineProps({
  deposit: Object
})

const depositStore = useDepositStore()
const accountStore = useAccountStore()
const liked = ref(false)

onMounted(async () => {
  try {
    const response = await axios.get(
      `${depositStore.API_URL}accounts/${accountStore.state.id}/liked-deposit/`,
      {
        headers: {
          Authorization: `Token ${accountStore.token}`
        }
      }
    );
    liked.value = response.data.some(deposit => deposit.id === props.deposit.id);
  } catch (error) {
    console.error(error);
  }
})

const toggleLike = async () => {
  if (!props.deposit) {
    console.error('deposit is undefined');
    return
  }
  try {
    if (accountStore.state.isAuthenticated === false) {
      Swal.fire({
        title: '로그인이 필요해요',
        icon: 'warning',
        confirmButtonText: 'YES'
      })
      return router.push({ name: 'LogInView' })
    }
    console.log(accountStore.state)
    await axios.post(
      `${depositStore.API_URL}finance/deposit/${props.deposit.id}/likes/`,
      {},
      {
        headers: {
          Authorization: `Token ${accountStore.token}`
        }
      }
    )
    liked.value = !liked.value
  } catch (error) {
    console.error(error)
  }
}

</script>

<style scoped>
.deposit-list-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 20px;
}

.card {
  width: 20rem;
  height: 18rem;
  border-radius: 25px;
  overflow: hidden;
  border: 0;
  margin-bottom: 30px;
  background-color: rgb(253, 251, 237);
}

.card-parent {
  box-shadow: 0 2px 6px;
  transition: transform 0.8s ease, box-shadow 0.8s ease;
}

.card-parent:hover {
  transform: translateY(-30px);
  box-shadow: 0 4px 12px;
  z-index: 1;
}

.card-body {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  height: 100%;
  padding: 1rem;
}

.card-logo-and-title {
  display: flex;
  align-items: center;
}

.company-image {
  width: 70px;
  height: 80px;
}

.card-titles {
  margin-left: 10px;
}

.card-text {
  margin-bottom: 0.5rem;
}

.content {
  margin-top: 20px;
  /* 상단 여백 추가 */
}

.card-actions {
  width: 100%;
  display: flex;
  justify-content: space-between;
  margin-top: auto;
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

.bank-modal-image {
  width: 150px;
}
</style>

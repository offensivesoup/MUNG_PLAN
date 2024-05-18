<!-- 
  what : 상세 페이지! 
 -->
 
 <template>
  <div class="adopt-dog-detail">
    <h1>DetailView</h1>
    <div v-if="dog">
      <p>{{ dog.id }}</p>
      <p>{{ dog.title }}</p>
      <p>{{ dog.content }}</p>
      <p>{{ dog.created_at }}</p>
      <p>{{ dog.updated_at }}</p>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useAdoptStore } from '@/stores/adopt'
import { useRoute } from 'vue-router'

const store = useAdoptStore()
const route = useRoute()
const dog = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}life/adopt/${route.params.id}/`
  })
    .then((response) => {
      console.log(response)
      dog.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
})
</script>

<style scoped>

</style>
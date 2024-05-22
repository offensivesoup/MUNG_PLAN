<template>
    <div>
        <h1>Create Dog</h1>
        <form @submit.prevent="createDog">
            <label for="name">Name:</label>
            <input type="text" id="name" v-model="dog.name" required>
            <br>
            <label for="age">Age:</label>
            <input type="number" id="age" v-model="dog.age" required>
            <br>
            <label for="gender">Gender:</label>
            <select id="gender" v-model="dog.gender" required>
                <option value="M">남아</option>
                <option value="F">여아</option>
                <option value="Q">중성화 수술 완료</option>
            </select>
            <br>
            <label for="birth_date">Birth Date:</label>
            <input type="date" id="birth_date" v-model="dog.birth_date" required>
            <br>
            <label for="type">Type:</label>
            <select id="type" v-model="dog.type" required>
                <option value="maltese">말티즈</option>
                <option value="Poodle">푸들</option>
                <option value="pomeranian">포메라니안</option>
                <option value="Shih Tzu">시츄</option>
                <option value="Bichon Frise">비숑프리제</option>
                <option value="Yorkshire Terrier">요크셔테리어</option>
                <option value="Jindo">진도견</option>
                <option value="Chihuahua">치와와</option>
                <option value="Spitz">스피츠</option>
                <option value="Dachshund">닥스훈트</option>
                <option value="Retriever">리트리버</option>
                <option value="Etc">기타</option>
            </select>
            <br>
            <button type="submit">Create</button>
        </form>
    </div>
</template>

<script setup>
import { useAccountStore } from '@/stores/account'
import { ref } from 'vue'
import axios from 'axios'

const store = useAccountStore()
const dog = ref({
    name: '',
    age: null,
    gender: '',
    birth_date: '',
    type: '',
})

const createDog = () => {
    axios.post(`${store.API_URL}accounts/${store.state.id}/dogs/`, dog.value)
        .then(response => {
            // Handle success
            console.log(response.data);
            // Redirect to the dog list page or do something else
        })
        .catch(error => {
            // Handle error
            console.error(error);
        })
}
</script>

<style scoped>

</style>
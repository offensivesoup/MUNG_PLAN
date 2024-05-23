<template>
  <div class="custom-dropdown">
    <label class="dropdown-label">{{ defaultLabel }}</label>
    <select v-model="selected" @change="emitValue">
      <option value="">{{ defaultLabel }}</option>
      <option v-for="option in options" :key="option.value" :value="option.value">{{ option.label }}</option>
    </select>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';

const props = defineProps({
  modelValue: {
    type: String,
    default: ''
  },
  options: {
    type: Array,
    required: true
  },
  defaultLabel: {
    type: String,
    required: true
  }
});

const emit = defineEmits(['update:modelValue']);

const selected = ref(props.modelValue);

watch(selected, (newValue) => {
  emit('update:modelValue', newValue);
});

const emitValue = () => {
  emit('update:modelValue', selected.value);
};
</script>

<style scoped>
.custom-dropdown {
  position: relative;
  display: flex;
  flex-direction: column;
  margin: 10px 0;
  width: 100%;
}

.custom-dropdown .dropdown-label {
  margin-bottom: 5px;
  color: #000;
  font-size: 1rem;
  font-weight: bold;
}

.custom-dropdown select {
  width: 100%;
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #f8f8f8;
  color: #333;
  outline: none;
  transition: border-color 0.3s;
}

.custom-dropdown select:focus {
  border-color: #888;
}

.custom-dropdown select option {
  color: #333;
}
</style>

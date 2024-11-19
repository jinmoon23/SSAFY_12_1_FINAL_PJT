import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useAuthStore } from './auth'

export const useUserInterestStore = defineStore('stock', () => {
  const store = useAuthStore()

  return {}
},{persist: true}
)

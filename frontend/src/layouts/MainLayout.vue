<template>
  <q-layout view="lhr lpR lFr">
    <q-header class="bg-white text-black">
      <q-toolbar class="text-center">
        <q-toolbar-title class="flex flex-center">
          <p class="text-primary q-my-none text-bold">m</p>
          <p class="q-my-none">Lekarz</p>
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import { v4 } from 'uuid'

if (localStorage.getItem('user_token') == undefined) {
  console.log('Eh')
  localStorage.setItem('user_token', v4())
}
</script>

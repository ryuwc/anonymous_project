<template>
  <div class="watch-list">
    <h1>보고싶은 영화</h1>
    <WatchListForm/>
  </div>
</template>

<script>
import WatchListForm from '@/components/WatchListForm.vue';

export default {
  name: 'WhtchListView',
  components: {
    WatchListForm
  }
}

</script>

<style>

</style>
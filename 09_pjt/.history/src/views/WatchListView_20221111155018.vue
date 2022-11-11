<template>
  <div class="d-flex flex-column">
    <h1><b>보고싶은 영화</b></h1>
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
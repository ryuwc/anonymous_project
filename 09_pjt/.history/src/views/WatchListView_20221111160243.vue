<template>
  <div class="d-flex flex-column align-items-center justify-contents-center">
    <div id="boss" class="bg-black d-flex flex-column align-items-center justify-contents-center">
      <h1><b>보고싶은 영화</b></h1>
      <WatchListForm class="mt-3 " />
    </div>
  </div>
</template>

<script>
import WatchListForm from "@/components/WatchListForm.vue";

export default {
  name: "WhtchListView",
  components: {
    WatchListForm,
  },
};
</script>

<style>
#boss {
  border-radius: 10px;
}
</style>

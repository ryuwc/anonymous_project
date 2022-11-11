<template>
  <div class="d-flex flex-column align-items-center justify-contents-center">
    <div id="boss" class="d-flex flex-column align-items-center justify-contents-center">
      <h1><b>보고싶은 영화</b></h1>
      <WatchListForm class="mt-3 " />
      <hr>
      <WatchListItem/>
    </div>
  </div>
</template>

<script>
import WatchListForm from "@/components/WatchListForm.vue";
import WatchListItem from "@/components/WatchListItem.vue";

export default {
  name: "WhtchListView",
  components: {
    WatchListForm,
    WatchListItem,
  },
};
</script>

<style scoped>
#boss {
  /* background-color: ; */
  border-radius: 8px;
}
</style>

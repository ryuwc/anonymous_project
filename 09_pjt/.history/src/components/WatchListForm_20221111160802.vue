<template>
    <div class="m-auto">
      <input
        type="text"
        class="form-control"
        placeholder="보고싶은 영화를 작성하세요!"
        style="width: 45vw"
        v-model.trim="wantMovie"
        @keyup.enter="createWantMovie"
      />
    </div>
</template>

<script>
export default {
  name: "WatchListForm",

  data() {
    return {
      wantMovie: '',
    };
  },

  mounted() {
    
  },

  methods: {
    createWantMovie() {
      if (!this.wantMovie) return
      this.$store.dispatch('createWantMovie', this.wantMovie)
    }
  },
};
</script>

<style></style>

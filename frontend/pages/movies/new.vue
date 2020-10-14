<template>
    <div class="container pt-5">
      <h1>New Movie</h1>
      <form class="mt-2" @submit="newMovie" method="POST">
        <div class="form-group">
          <label for="title">Title:</label>
          <input type="text" v-model="form.title" class="form-control" placeholder="Enter title of movie" id="title">
        </div>
        <div class="form-group">
          <label for="release_date">Release date:</label>
          <input type="date" v-model="form.release_date" class="form-control" placeholder="Enter title of movie" id="release_date">
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>

    </div>
</template>

<script>
export default {
  data: () => ({
    form: {
      title: null,
      release_date: null
    }
  }),
  methods: {
    newMovie(e) {
      e.preventDefault()
      this.$store.dispatch('movies/new', this.form)
      .then((res) => {
        console.log('res = ', res);
      })
    }
  },
}
</script>

<style>

</style>

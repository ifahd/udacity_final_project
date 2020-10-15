<template>
    <div class="container pt-5">
      <h1>Edit Movie</h1>
      <form class="mt-2" @submit="update" method="POST">
        <div class="form-group">
          <label for="title">Title:</label>
          <input type="text" v-model="movie.title" class="form-control" placeholder="Enter title of movie" id="title">
        </div>
        <div class="form-group">
          <label for="release_date">Release date:</label>
          <input type="date" placeholder="dd-mm-yyyy" value=""
        min="1997-01-01" max="2030-12-31"  v-model="movie.release_date" class="form-control" id="release_date">
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>

    </div>
</template>

<script>
export default {
  computed: {
    movie () {
      return Object.assign({}, this.$store.getters['movies/movie'])
    }
  },
  created () {
    this.$store.dispatch('movies/get', this.$route.params.id)
  },
  methods: {
    update(e) {
      e.preventDefault()
      this.$store.dispatch('movies/update', this.movie)
      .then((res) => {
        this.$Toast.fire({
          icon: 'success',
          title: 'Updated successfully'
        })

        this.$router.push({ name: 'movies' })
      })
    }
  },
}
</script>

<style>

</style>

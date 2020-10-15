<template>
  <div>
    <div class="container pt-5">
      <h1>Movie: {{ movie.title }}</h1>
      <router-link :to="{name: 'movies-edit-id', params: { id: movie.id }}" class="btn btn-primary">
        Edit
      </router-link>
      <table class="table table-bordered mt-2">
        <tbody>
          <tr>
            <th>ID</th>
            <td>{{ movie.id }}</td>
          </tr>
          <tr>
            <th>Title</th>
            <td>{{ movie.title }}</td>
          </tr>
          <tr>
            <th>Release date</th>
            <td>{{ movie.release_date }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
  export default {
    computed: {
      movie () {
        return this.$store.getters['movies/movie']
      }
    },
    created () {
      this.$store.dispatch('movies/get', this.$route.params.id)
    },

  }
</script>

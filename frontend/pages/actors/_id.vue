<template>
  <div>
    <div class="container pt-5">
      <h1>Actor: {{ actor.name }}</h1>
      <router-link :to="{name: 'actors-edit-id', params: { id: actor.id }}" class="btn btn-primary">
        Edit
      </router-link>
      <table class="table table-bordered mt-2">
        <tbody>
          <tr>
            <th>ID</th>
            <td>{{ actor.id }}</td>
          </tr>
          <tr>
            <th>Name</th>
            <td>{{ actor.name }}</td>
          </tr>
          <tr>
            <th>Gender</th>
            <td>{{ actor.gender }}</td>
          </tr>
          <tr>
            <th>Gender</th>
            <td>{{ actor.age }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
  export default {
    computed: {
      actor () {
        return this.$store.getters['actors/actor']
      }
    },
    created () {
      this.$store.dispatch('actors/get', this.$route.params.id)
    },

  }
</script>

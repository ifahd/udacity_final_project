<template>
    <div class="container pt-5">
      <h1>Edit Actor</h1>
      <form class="mt-2" @submit="update" method="POST">
        <div class="form-group">
          <label for="name">Name:</label>
          <input type="text" v-model="actor.name" class="form-control" placeholder="Enter name of actor" id="name">
        </div>
        <div class="form-group">
          <label for="age">Age:</label>
          <input type="number" placeholder="Age" v-model="actor.age" class="form-control" id="age">
        </div>
        <div class="form-group">
          <label for="gender">Gender:</label>
          <select class="form-control" id="gender" v-model="actor.gender">
            <option value="Male">Male</option>
            <option value="Female">Female</option>
          </select>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>

    </div>
</template>

<script>
export default {
  computed: {
    actor () {
      return Object.assign({}, this.$store.getters['actors/actor'])
    }
  },
  created () {
    this.$store.dispatch('actors/get', this.$route.params.id)
  },
  methods: {
    update(e) {
      e.preventDefault()
      this.$store.dispatch('actors/update', this.actor)
      .then((res) => {
        this.$Toast.fire({
          icon: 'success',
          title: 'Updated successfully'
        })

        this.$router.push({ name: 'actors' })
      })
    }
  },
}
</script>

<style>

</style>

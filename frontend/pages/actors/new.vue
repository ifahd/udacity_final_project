<template>
    <div class="container pt-5">
      <h1>New Movie</h1>
      <form class="mt-2" @submit="newActor" method="POST">
        <div class="form-group">
          <label for="name">Name:</label>
          <input type="text" v-model="form.name" class="form-control" placeholder="Enter name of actor" id="name">
        </div>
        <div class="form-group">
          <label for="age">Age:</label>
          <input type="number" placeholder="Age" v-model="form.age" class="form-control" id="age">
        </div>
        <div class="form-group">
          <label for="gender">Gender:</label>
          <select class="form-control" id="gender" v-model="form.gender">
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
  data: () => ({
    form: {
      name: null,
      age: null,
      gender: null,
    }
  }),
  methods: {
    newActor(e) {
      e.preventDefault()
      this.$store.dispatch('actors/create', this.form)
      .then((res) => {
        this.$Toast.fire({
          icon: 'success',
          title: 'Created successfully'
        })
        this.form = {
          name: null,
          age: null,
          gender: null,
        }
        this.$router.push({ name: 'actors' })
      })

    }
  },
}
</script>

<style>

</style>

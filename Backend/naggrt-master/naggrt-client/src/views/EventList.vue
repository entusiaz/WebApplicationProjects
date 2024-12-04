<template>
  <div class="home container-fluid h-100">
    <!-- <HelloWorld msg="Welcome to Your Vue.js App" /> -->
    <div class="row">
      <v-row align="center" justify="center">
        <div class="col-md-5">
          <Carousel />
          <EventCard />
        </div>
      </v-row>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
//import HelloWorld from "@/components/HelloWorld.vue";
import Carousel from "@/components/Carousel.vue";
import EventCard from "@/components/EventCard.vue";
export default {
  name: "Home",
  components: {
    // HelloWorld
    Carousel,
    EventCard
  }
};
</script>

<style scoped></style>

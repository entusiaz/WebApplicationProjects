<template>
  <v-container>
    <!-- <v-row class="text-center">
      <v-col cols="12">
        <v-img
          :src="require('../assets/patorankingCrowd.jpg')"
          class="my-3"
          contain
          height="200"
        />
      </v-col>
    </v-row>-->

    <v-row align="center" justify="center">
      <!-- <v-carousel>
        <v-carousel-item
          v-for="(item, i) in items"
          :key="i"
          :src="item.src"
          reverse-transition="fade-transition"
          transition="fade-transition"
        ></v-carousel-item>
      </v-carousel>-->

      <v-card
        elevation="0"
        max-width="300"
        max-height="300"
        class="mx-auto"
        outlined
      >
        <div :continuous="true">
          <v-carousel cycle height="280">
            <v-carousel-item
              v-for="(item, i) in items"
              :key="i"
              reverse-transition="fade-transition"
              transition="fade-transition"
            >
              <img :src="item.src" height="280" />
            </v-carousel-item>
          </v-carousel>
        </div>
      </v-card>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "Carousel",
  // props: {},

  data() {
    return {
      items: [
        {
          src: require("../assets/patorankingCrowd.jpg"),
          handle: "Alagba Lubomi"
        },
        {
          src: require("../assets/johnBoyega.jpg"),
          handle: "Ox"
        }
      ],

      colors: [
        "green",
        "secondary",
        "yellow darken-4",
        "red lighten-2",
        "orange darken-1"
      ],
      cycle: false,
      slides: ["First", "Second", "Third", "Fourth", "Fifth"]
    };
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/* Make the image fully responsive */
.carousel-inner img {
  width: 100%;
  height: 100%;
}
</style>

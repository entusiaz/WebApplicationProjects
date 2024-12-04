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

    <v-row>
      <!-- <v-carousel>
        <v-carousel-item
          v-for="(item, i) in items"
          :key="i"
          :src="item.src"
          reverse-transition="fade-transition"
          transition="fade-transition"
        ></v-carousel-item>
      </v-carousel>-->

      <v-card elevation="4" max-width="444" class="mx-auto">
        <!-- <v-system-bar lights-out></v-system-bar> -->
        <!-- <v-carousel
        :continuous="false"
        :cycle="cycle"
        :show-arrows="false"
        hide-delimiter-background
        delimiter-icon="mdi-minus"
        height="300"
      >
        <v-carousel-item v-for="(slide, i) in slides" :key="i">
          <v-sheet :color="colors[i]" height="100%" tile>
            <v-row class="fill-height" align="center" justify="center">
              <div class="display-3">{{ slide }} Slide</div>
            </v-row>
          </v-sheet>
        </v-carousel-item>
        </v-carousel>-->
        <div>
          <v-carousel height="300">
            <v-carousel-item
              v-for="(item, i) in items"
              :key="i"
              reverse-transition="fade-transition"
              transition="fade-transition"
            >
              <img :src="item.src" height="350" />
              <v-list two-line>
                <v-list-item>
                  <v-list-item-avatar>
                    <v-img src="https://cdn.vuetifyjs.com/images/john.png"></v-img>
                  </v-list-item-avatar>
                  <v-list-item-content>
                    <v-list-item-title>{{ author }}</v-list-item-title>
                    <!-- <v-list-item-subtitle>Author</v-list-item-subtitle> -->
                  </v-list-item-content>
                </v-list-item>
              </v-list>
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
          src: require("../assets/patorankingCrowd.jpg"),
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

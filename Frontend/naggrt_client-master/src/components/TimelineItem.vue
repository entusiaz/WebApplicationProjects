<template>
  <div class="body">
    <v-container>
      <v-row>
        <v-col cols="12">
          <v-card class="pt-n16 mb-n10 pb-4 mx-auto card" outlined>
            <v-card-title class="mt-n6">
              <div class="text-left">
                <a href="#">
                  <v-icon class="mb-n6 report-button">block</v-icon>
                </a>
              </div>
            </v-card-title>
            <!--  </v-card-title> -->

            <span
              class="d-inline-block font-weight-light text-left"
              style="max-width: 94%; font-size: 14px; margin-left: 5%"
              >{{ timeline.desc }}</span
            >
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "TimelineItem",
  props: {
    timeline: Object
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.remove-underline {
  text-decoration: none;
}
.card {
  background-color: rgb(243, 243, 250);
}
.card:hover {
  border: 1px solid rgb(152, 152, 179);
}

/* selected link */
.card:active {
  border: 1px solid rgb(152, 152, 179);
  background-color: rgb(245, 245, 245);
}
.report-button {
  color: crimson;
}
.report-button:hover {
  color: crimson;
  box-shadow: 0.2em 0.1em solid rgb(221, 221, 221);
}
.report-button:active {
  color: crimson;
  box-shadow: 0.1em 0.1em 0.2em 0.1em rgb(221, 221, 221);
}
</style>

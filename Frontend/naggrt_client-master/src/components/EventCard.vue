<template>
  <div class="body">
    <router-link
      class="remove-underline"
      :to="{ name: 'event-timeline', params: { id: event.id, event: event } }"
    >
      <v-container>
        <v-row>
          <v-col cols="12">
            <v-card class="mb-n4 mx-auto card" outlined>
              <v-card-title>
                <div class="text-left">
                  <v-icon small left>mdi-twitter</v-icon>
                  <span
                    class="font-weight-regular text-left"
                    style="max-width: 270px; font-size: 16px; "
                    >{{ event.title }}</span
                  >
                </div>
              </v-card-title>
              <!--  </v-card-title> -->
              <span></span>
              <span
                class="d-inline-block font-weight-light text-left"
                style="max-width: 80%; font-size: 14px; margin-left: 5%"
                >{{ event.desc }}</span
              >

              <v-card-actions style="max-width: 90%;">
                <v-list-item class="grow">
                  <v-list-item-avatar color="grey darken-3">
                    <v-img
                      class="elevation-6 small"
                      src="https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=White&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light"
                    ></v-img>
                  </v-list-item-avatar>

                  <v-list-item-content>
                    <p class="small mt-4">{{ event.author }}</p>
                  </v-list-item-content>

                  <v-row align="center" justify="end">
                    <v-icon class="small mr-1">mdi-heart</v-icon>
                    <span class="small subheading mr-2">{{ event.likes }}</span>
                    <span class="mr-1">·</span>
                    <v-icon class="small mr-1">mdi-share</v-icon>
                    <span class="small subheading">{{ event.shares }}</span>
                  </v-row>
                </v-list-item>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </router-link>
  </div>
</template>

<script>
export default {
  name: "EventCard",
  props: {
    event: Object
  }
};
</script>

<style scoped>
.remove-underline {
  text-decoration: none;
}

/* mouse over link */
.card:hover {
  border: 1px solid navy;
}

/* selected link */
.card:active {
  border: 1px solid navy;
  background-color: rgb(245, 245, 245);
}
</style>

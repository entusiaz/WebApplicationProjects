<template>
  <h1>this is a timeline of selected {{ id }} event</h1>
</template>
<script>
export default {
  data() {
    return {
      props: ["id"]
    };
  }
};
</script>

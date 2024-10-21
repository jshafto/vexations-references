<template>
  <div class="container" id="additional">
    <nuxt-link :to="anchorDestination" class="jump" external
      >Back to references table</nuxt-link
    >
    <div class="h2">Additional References</div>
    <div v-for="item in additional" :key="item.id" class="quote-block">
      <div class="quote-text" v-html="item.quote"></div>
      <div class="source-info">
        <span v-if="item.author">– {{ item.author }}</span
        ><span v-if="item.author && item.additional">, </span
        ><span v-if="item.additional">{{ item.additional }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import additional from "~/public/additional";
// const prefixString = import.meta.env.PROD ? "/vexations-references/" : "/";
const anchorDestination = import.meta.env.PROD
  ? {
      path: "https://annelysegelman.com/vexations-references/",
      hash: "#top",
    }
  : { name: "home", hash: "#top" };
</script>

<style scoped>
.container {
  margin-top: 80px;
  padding-left: 50px;
  padding-right: 50px;
}
.h2 {
  font-size: 24px;
  font-weight: normal;
  margin-bottom: 20px;
}

a {
  text-decoration-color: transparent;
  transition: text-decoration-color 150ms ease;
  color: #0071c5;
}
a:hover {
  text-decoration-color: #0071c5;
}

.jump {
  font-weight: normal;
  display: block;
  font-style: italic;
  margin-bottom: 16px;
}

.quote-block {
  margin-bottom: 24px;
}
.quote-text {
  margin-bottom: 8px;
}

.source-info {
  padding-left: 50px;
}
</style>

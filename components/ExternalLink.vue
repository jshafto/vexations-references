<template>
  <svg
    xmlns="http://www.w3.org/2000/svg"
    width="1em"
    height="1em"
    viewBox="0 0 24 24"
    stroke-linecap="round"
    stroke-linejoin="round"
    stroke-width="2"
    fill="none"
    :class="props.purple ? 'purple' : ''"
  >
    <path d="M11 5h-6v14h14v-6"></path>
    <path d="M13 11l7 -7"></path>
    <path d="M21 3h-6M21 3v6"></path>
  </svg>
</template>

<script setup>
const props = defineProps({
  purple: {
    default: false,
    type: Boolean,
  },
});
</script>

<style scoped>
svg {
  vertical-align: middle;
  padding-bottom: 4px;
  stroke: #0071c5;
  color: #0071c5;
}
.purple svg,
svg.purple {
  stroke: #823061;
  color: #823061;
}

@media (prefers-color-scheme: dark) {
  .purple svg,
  svg.purple {
    stroke: #d793bc;
    color: #d793bc;
  }
}
</style>

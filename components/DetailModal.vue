<template>
  <div class="modal-contents" @click.stop>
    <div class="modal-actions">
      <button class="close-button" @click.stop="emits('close')">
        <CloseIcon />
      </button>
    </div>
    <div class="modal-text" v-html="props.modalContent"></div>
    <img
      v-if="props.picture"
      :src="`${prefixString}${props.picture}`"
      :alt="props.picture"
      class="media"
    />
    <div class="author" v-if="props.author">— {{ author }}</div>
    <div class="source" v-if="props.source">{{ source }}</div>
  </div>
</template>

<script setup>
import CloseIcon from "./CloseIcon.vue";

const props = defineProps({
  modalContent: {
    type: String,
    default: "",
  },
  picture: { type: String, default: "" },
  author: { type: String, default: "" },
  source: { type: String, default: "" },
});

const emits = defineEmits(["close"]);

const prefixString = import.meta.env.PROD
  ? "/vexations-references/media/"
  : "/media/";
</script>

<style scoped>
.modal-contents {
  background-color: white;
  border: 1px black solid;
  max-width: 70%;
  padding: 0px 44px 24px 44px;
  border-radius: 8px;
  position: relative;
  max-height: 80%;
  overflow-y: scroll;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.modal-actions {
  position: sticky;
  top: 0px;
  width: 100%;
  display: flex;
  justify-content: flex-end;
  padding-top: 8px;
  padding-bottom: 4px;
}

.close-button {
  transform: translateX(36px);
  height: 24px;
  width: 24px;
  border-radius: 16px;
  cursor: pointer;
  transition: background-color ease-in-out 150ms;
  border: none;
  background-color: transparent;
  display: flex;
  align-items: center;
  justify-content: center;
}
.close-button:hover {
  background-color: #00000018;
}

.media {
  max-width: 100%;
  max-height: 60dvh;
  margin-bottom: 16px;
  align-self: center;
}

.modal-text {
  max-width: 550px;
  margin: 0 auto;
  font-family: Baskervville, serif;
  margin-bottom: 16px;
}

.source {
  font-style: italic;
  font-family: Baskervville, serif;
}
.author {
  font-family: Baskervville, serif;
}

@media (prefers-color-scheme: dark) {
  .modal-contents {
    background-color: rgb(36, 36, 36);
    border: 1px #ffffff70 solid;
  }
  .close-button:hover {
    background-color: #ffffff18;
  }
}
</style>

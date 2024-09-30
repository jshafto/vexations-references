<template>
  <div class="table-wrapper" @keyup.esc="closeModal">
    <table class="full-table">
      <thead>
        <tr>
          <th class="headers"></th>
          <th
            v-for="col in headers"
            :key="col"
            class="headers"
            v-html="col"
          ></th>
        </tr>
        <tr>
          <th class="header-divider" colspan="7"></th>
        </tr>
      </thead>
      <tbody class="text">
        <tr
          v-for="row in citations"
          :key="row.id"
          @click="openModal(row)"
          class="row"
          :class="hasContent(row) ? 'clickable' : 'not-clickable'"
        >
          <td class="table-cell">
            <span v-if="hasContent(row)"
              ><PaperclipIcon class="paperclip"
            /></span>
          </td>
          <td v-for="col in headers" :key="col" class="table-cell cols">
            <span v-if="col === 'Referenced'">
              <a v-if="row.Link && row[col]" :href="row.Link" target="_blank">
                {{ row[col] }}
                <ExternalLink />
              </a>
              <span v-else-if="!row.Link">
                {{ row[col] }}
              </span>
              <a v-else :href="row.Link" target="_blank">
                <span class="see-more">(See more)</span> <ExternalLink
              /></a>
            </span>
            <span
              v-else-if="col.includes('Line')"
              v-html="row[col]"
              class="full-line"
            ></span>
            <span v-else>{{ row[col] }}</span>
          </td>
        </tr>
      </tbody>
    </table>
    <div
      v-if="modal"
      class="hover-el"
      @click="closeModal"
      ref="modalref"
      tabindex="0"
    >
      <DetailModal
        :author="author"
        :source="source"
        :modal-content="modalContent"
        :picture="picture"
        @close="closeModal"
      />
    </div>
  </div>
</template>

<script setup>
import citations from "~/vexations.js";
import ExternalLink from "./ExternalLink.vue";
import PaperclipIcon from "./PaperclipIcon.vue";
import DetailModal from "./DetailModal.vue";

const picture = ref("");
const modalContent = ref("");
const author = ref("");
const source = ref("");
const modalref = ref(null);
const modal = ref(false);
const openModal = (row) => {
  if (hasContent(row)) {
    modal.value = true;
    picture.value = row["File"];
    modalContent.value = row["Hover element"];
    author.value = row["Author"];
    source.value = row["Referenced"];
    nextTick(() => {
      modalref.value.focus();
    });
  }
};

const closeModal = () => {
  modal.value = false;
  picture.value = "";
  author.value = "";
  source.value = "";
};

const hasContent = (row) => {
  return !!row["File"] || !!row["Hover element"];
};

const headers = Object.keys(citations[0]).filter(
  (item) =>
    item !== "id" &&
    item !== "Hover element" &&
    item !== "File" &&
    item !== "Link" &&
    item !== ""
);
</script>

<style scoped>
a {
  text-decoration-color: transparent;
  transition: text-decoration-color 150ms ease;
  color: #0071c5;
}
a:hover {
  text-decoration-color: #0071c5;
}
.see-more {
  font-style: italic;
}

.full-table {
  text-align: left;
  position: relative;
  padding: 0px;
  border-collapse: collapse;
}

.table-cell {
  padding: 14px 0px;
  border: none;
  border-spacing: 0;
  overflow: hidden;
}

.headers {
  background: white;
  position: sticky;
  top: 2px;
  padding-top: 10px;
  padding-bottom: 10px;
  transform: translateY(-3px);
  border: none;
  border-spacing: 0;
  height: 44px;
}

.table-wrapper {
  max-height: calc(100vh - 60px);
  overflow: auto;
}

.full-line {
  min-width: 250px;
}

.cols {
  padding-right: 10px;
  padding-left: 12px;
}

.hover-el {
  position: absolute;
  top: 0;
  height: 100vh;
  width: 100vw;
  background-color: #00000088;
  display: flex;
  align-items: center;
  justify-content: center;
}
.row {
  border-bottom: 1px solid rgba(0, 0, 0, 0.17);
}
.row:hover {
  transition: background-color ease-in-out 150ms;
  background-color: #ffffb7;
}
.clickable {
  cursor: pointer;
}
.not-clickable {
  cursor: default;
}

.header-divider {
  background-color: black;
  height: 1px;
  padding: 0px;
  position: sticky;
  top: 69px;
  transform: translateY(-6px);
}

.headers {
  padding: 10px;
}

.paperclip {
  padding-left: 10px;
  padding-right: 10px;
}

@media (prefers-color-scheme: dark) {
  .headers {
    background: rgb(27, 27, 27);
  }
  .row:hover {
    background-color: #303022;
  }
  .row {
    border-bottom: 1px solid rgba(255, 255, 255, 0.17);
  }
  .header-divider {
    background-color: rgb(190, 190, 190);
  }
}
</style>

const path = require("path");

const dist_path = "trackash/static/js/dist";

module.exports = {
  entry: "./trackash/static/js/index.js",
  output: {
    filename: "main.js",
    path: path.resolve(__dirname, `${dist_path}`),
  },
  resolve: {
    alias: {
      vue$: "vue/dist/vue.esm.js",
    },
  },
  watch: true,
};

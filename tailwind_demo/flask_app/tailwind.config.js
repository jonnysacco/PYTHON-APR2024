/** @type {import('tailwindcss').Config} */

module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/src/**/*.js"
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("daisyui"), 
    require('@tailwindcss/typography')
  ],
  daisyui: {
    themes: ["light", "dark", "retro"],
  },
}


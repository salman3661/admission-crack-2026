/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        chorcha: {
          bg: '#F6F8F6',
          primary: '#056839',
          secondary: '#00B09B',
          accent: '#96C93D',
          darkBg: '#0B110D',
          darkCard: '#131E17',
          darkBorder: '#1E2F24',
        },
        brand: {
          50: '#f0fdf4',
          100: '#dcfce7',
          200: '#bbf7d0',
          300: '#86efac',
          400: '#4ade80',
          500: '#10b981',
          600: '#056839',
          700: '#044e2b',
          800: '#033920',
          900: '#022415',
        }
      },
      fontFamily: {
        sans: ["'SolaimanLipi'", "'Hind Siliguri'", 'system-ui', 'sans-serif'],
        bengali: ["'SolaimanLipi'", "'Hind Siliguri'", 'sans-serif'],
        outfit: ['"Outfit"', 'sans-serif'],
      },
      boxShadow: {
        'glossy': '0 8px 30px rgba(0, 0, 0, 0.12), inset 0 1px 1px rgba(255, 255, 255, 0.4)',
        'glossy-hover': '0 14px 40px rgba(0, 0, 0, 0.18), inset 0 1px 1px rgba(255, 255, 255, 0.6)',
      }
    },
  },
  plugins: [],
}

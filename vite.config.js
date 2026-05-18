import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  root: '.',
  server: {
    port: 5173,
    open: true,
    host: true
  },
  build: {
    outDir: 'dist',
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        shop: resolve(__dirname, 'shop.html'),
        brands: resolve(__dirname, 'brands.html'),
        offers: resolve(__dirname, 'offers.html'),
        about: resolve(__dirname, 'about.html'),
        contact: resolve(__dirname, 'contact.html'),
        product: resolve(__dirname, 'product.html')
      }
    }
  }
});

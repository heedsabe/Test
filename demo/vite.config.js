import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { viteSingleFile } from 'vite-plugin-singlefile';

// `npm run build` で JS/CSS をすべてインライン化した単一HTML (standalone/index.html) を出力する。
// ダブルクリックで開けるので、展示会場などのオフライン環境でも固定シナリオ版はそのまま動く。
export default defineConfig({
  plugins: [react(), viteSingleFile()],
  build: { outDir: 'standalone', emptyOutDir: true },
});

# vial-web

## Building

```
git clone https://github.com/vial-kb/vial-web.git
cd vial-web
git clone https://github.com/vial-kb/vial-gui.git
git clone https://github.com/vial-kb/via-keymap-precompiled.git
./fetch-emsdk.sh
./fetch-deps.sh
./build-deps.sh
cd src
./build.sh
```

## Running locally

Emscripten builds that use pthreads require cross-origin isolation. Serve the
`src/build` folder with COOP/COEP headers or `SharedArrayBuffer` will be
undefined.

```
python3 serve.py --port 8000
```

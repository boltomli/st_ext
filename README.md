# SoundTouch ext

Refer to [ssrpc](https://github.com/boltomli/ssrpc) for main code.

## setup

```sh
git clone --depth=1 git@github.com:boltomli/st_ext.git
git submodule update --init --recursive
```

## build

```sh
mkdir build && cd build
conan install .. --build missing
cmake .. -DCMAKE_TOOLCHAIN_FILE=Release/generators/conan_toolchain.cmake -DCMAKE_BUILD_TYPE=Release
cmake --build .
```

## test

```python
import st_ext
audio_bytes = bytes(st_ext.stretch(list(b"wavedata"), 20))
```

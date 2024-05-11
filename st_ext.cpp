#include <nanobind/nanobind.h>
#include <nanobind/stl/vector.h>

using UCharVector = std::vector<unsigned char>;

#include "AudioFile.h"

void load_audio(const UCharVector &data) {
    AudioFile<float> audioFile;
    std::vector<unsigned char> waveData(data.size());
    for (size_t i = 0; i < data.size(); i++) {
        waveData[i] = data[i];
    }
    bool status = audioFile.loadFromMemory(waveData);
    audioFile.printSummary();
}

NB_MODULE(st_ext, m) {
    m.def("load_audio", &load_audio);
}

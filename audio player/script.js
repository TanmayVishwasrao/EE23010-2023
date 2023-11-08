document.addEventListener("DOMContentLoaded", function () {
    const audioPlayer = document.getElementById("audio-player");
    const playlist = document.getElementById("playlist");
    const currentSongName = document.getElementById("current-song");
    const prevButton = document.getElementById("prev-button");
    const nextButton = document.getElementById("next-button");

    const songs = playlist.querySelectorAll("li a");

    // Function to play a random song
    function playRandomSong() {
        const randomIndex = Math.floor(Math.random() * songs.length);
        const songUrl = songs[randomIndex].getAttribute("href");
        audioPlayer.src = songUrl;
        audioPlayer.load();
        audioPlayer.play();
        currentSongName.textContent = songs[randomIndex].textContent;
    }

    nextButton.addEventListener("click", function () {
        playRandomSong();
    });

    prevButton.addEventListener("click", function () {
        playRandomSong();
    });

    // Automatically play a random song when the current song ends
    audioPlayer.addEventListener("ended", function () {
        playRandomSong();
    });

    // Play a random song initially
    playRandomSong();
});

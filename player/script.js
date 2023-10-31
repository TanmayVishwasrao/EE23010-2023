document.addEventListener("DOMContentLoaded", function () {
    const audioPlayer = document.getElementById("audio-player");
    const playlist = document.getElementById("playlist");
    const prevButton = document.getElementById("prev-button");
    const nextButton = document.getElementById("next-button");
    const currentSongName = document.getElementById("current-song");

    let currentSongIndex = 0;

    const songs = playlist.querySelectorAll("li a");
    
    // Function to shuffle the playlist
    function shufflePlaylist() {
        for (let i = songs.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [songs[i].href, songs[j].href] = [songs[j].href, songs[i].href];
        }
    }
    
    shufflePlaylist();
    
    function playSong(index) {
        const songUrl = songs[index].getAttribute("href");
        audioPlayer.src = songUrl;
        audioPlayer.load();
        audioPlayer.play();
        currentSongIndex = index;
        currentSongName.textContent = songs[index].textContent;
    }

    nextButton.addEventListener("click", function () {
        currentSongIndex = (currentSongIndex + 1) % songs.length;
        playSong(currentSongIndex);
    });

    prevButton.addEventListener("click", function () {
        currentSongIndex = (currentSongIndex - 1 + songs.length) % songs.length;
        playSong(currentSongIndex);
    });

    // Automatically play the next song when the current song ends
    audioPlayer.addEventListener("ended", function () {
        currentSongIndex = (currentSongIndex + 1) % songs.length;
        playSong(currentSongIndex);
    });

    // Play a random song from the shuffled playlist
    playSong(currentSongIndex);
});

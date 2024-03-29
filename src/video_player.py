"""A video player class."""

from .video_library import VideoLibrary
from random import randint
from .video import Video


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        # self._playing = 0
        self._current_video = None
        self._pause = False
        self._playlists = {}
        self._playlist_cases = {}


    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        library = self._video_library.get_all_videos()
        library.sort(key=lambda x: x.title)
        for i in range(len(self._video_library.get_all_videos())):
            video = library[i]
            tags = " ".join(video.tags)
            if video._flag is True:
                print("{} ({}) [{}] - FLAGGED (reason: {})".format(video.title, video.video_id, tags, video._flag_reason))
            else:
                print("{} ({}) [{}]".format(video.title, video.video_id, tags))

    def play_video(self, video_id):
        """Plays the respective video.
        Args:
            video_id: The video_id to be played.
        """


        video = self._video_library.get_video(video_id)
        if not video:
            print("Cannot play video: Video does not exist")
            return
        if video._flag:
            print("Cannot play video: Video is currently flagged (reason: {})".format(video._flag_reason))
            return

        if self._current_video != None:
            print("Stopping video: {}".format(self._current_video.title))
            print("Playing video: {}".format(video.title))
            self._current_video = video
            self._pause = False
            return

        print("Playing video: {}".format(video.title))
        self._current_video = video
        self._pause = False



        # This code finds the video that we are trying to play and saves variable as current_vid
        # library = self._video_library.get_all_videos()
        # current_vid = library[0]
        # for vid in library:
        #     # print(vid)
        #     # print(vid.video_id)
        #     # print(video_id[1:-1])
        #     if vid.video_id == video_id[1:-1]:
        #         # print(vid.video_id)
        #         current_vid = vid
        #
        #
        #
        #
        # previously_playing = self._playing
        # if previously_playing != 0:
        #     prev_vid = library[0]
        #     print(self._playing)
        #     for vid in library:
        #         if vid.video_id == previously_playing[1:-1]:
        #             prev_vid = vid
        #     print("Stopping video: {}".format(prev_vid.title))
        # self._playing = video_id
        # print("Playing video: {}".format(current_vid.title))


    def stop_video(self):
        """Stops the current video."""
        if self._current_video is None:
            print("Cannot stop video: No video is currently playing")
            return
        else:
            print("Stopping video: {}".format(self._current_video.title))
            self._current_video = None

    def play_random_video(self):
        """Plays a random video from the video library."""
        library = list(self._video_library.get_all_videos())
        for i in range(len(library)-1, -1, -1):
            video = library[i]
            if video._flag is True:
                library.remove(video)
        if len(library) == 0:
            print("No videos available")
            return
        # for video in library:
        #     print(video._title)
        #     print(video._flag)
        #     if video._flag:
        #         library.remove(video)
        #         print(video.title)
        print(len(library))
        rand_index = randint(0, len(library)-1)
        rand_video = library[rand_index]
        # print(library)

        if self._current_video != None:
            print("Stopping video: {}".format(self._current_video.title))
            print("Playing video: {}".format(rand_video.title))
            self._current_video = rand_video
            self._pause = False
            return
        print("Playing video: {}".format(rand_video.title))
        self._current_video = rand_video
        self._pause = False





    def pause_video(self):
        """Pauses the current video."""
        if self._pause:
            print("Video already paused: {}".format(self._current_video.title))
        elif self._current_video is None:
            print("Cannot pause video: No video is currently playing")
        else:
            print("Pausing video: {}".format(self._current_video.title))
            self._pause = True


    def continue_video(self):
        """Resumes playing the current video."""
        if self._current_video is None:
            print("Cannot continue video: No video is currently playing")
        elif not self._pause:
            print("Cannot continue video: Video is not paused")
        else:
            print("Continuing video: {}".format(self._current_video.title))
            self._pause = False



    def show_playing(self):
        """Displays video currently playing."""
        if self._current_video is None:
            print("No video is currently playing")
        elif self._pause is True:
            print("Currently playing: {} ({}) [{}] - PAUSED".format(self._current_video.title,
                  self._current_video.video_id, " ".join(self._current_video.tags)))
        else:
            print("Currently playing: {} ({}) [{}]".format(self._current_video.title,
                                                           self._current_video.video_id, " ".join(self._current_video.tags)))



    def create_playlist(self, playlist_name): # Might still need to sort out whitespace issue
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        check_list = list(self._playlists.keys())
        display_name = playlist_name.lower()
        if display_name in check_list:
            print("Cannot create playlist: A playlist with the same name already exists")
            return
        self._playlists[display_name] = []
        self._playlist_cases[playlist_name] = []
        print("Successfully created new playlist: {}".format(playlist_name))

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        video = self._video_library.get_video(video_id)
        display_name = playlist_name.lower()
        # if video._flag:
        #     print("Cannot add video to {}: Video is currently flagged (reason: {})".format(playlist_name, video._flag_reason))
        #     return
        if display_name not in self._playlists:
            print("Cannot add video to {}: Playlist does not exist".format(playlist_name))
            return
        if video_id not in list(self._video_library._videos.keys()):
            print("Cannot add video to {}: Video does not exist".format(playlist_name))
            return
        if video._flag:
            print("Cannot add video to {}: Video is currently flagged (reason: {})".format(playlist_name, video._flag_reason))
            return

        if video_id in self._playlists[display_name]:
            print("Cannot add video to {}: Video already added".format(playlist_name))
            return
        else:
            self._playlists[display_name].append(video_id)
            print("Added video to {}: {}".format(playlist_name, self._video_library.get_video(video_id).title))

    def show_all_playlists(self):
        """Display all playlists."""
        if self._playlists == {}:
            print("No playlists exist yet")
            return
        playlist_name_list = list(self._playlist_cases.keys())
        playlist_name_list.sort()
        print("Showing all playlists:")
        for name in playlist_name_list:
            print(name)


    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        display_name = playlist_name.lower()
        if display_name not in self._playlists:
            print("Cannot show playlist {}: Playlist does not exist".format(playlist_name))
            return
        if not self._playlists[display_name]:
            print("Showing playlist: {}".format(playlist_name))
            print("No videos here yet")
            return
        print("Showing playlist: {}".format(playlist_name))
        for url in self._playlists[display_name]:
            video = self._video_library.get_video(url)
            tags = " ".join(video.tags)
            if video._flag is True:
                print("{} ({}) [{}] - FLAGGED (reason: {})".format(video.title, video.video_id, tags, video._flag_reason))
            else:
                print("{} ({}) [{}]".format(video.title, video.video_id, tags))


    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        display_name = playlist_name.lower()
        if display_name not in self._playlists:
            print("Cannot remove video from {}: Playlist does not exist".format(playlist_name))
            return
        video = self._video_library.get_video(video_id)
        if video not in self._video_library.get_all_videos():
            print("Cannot remove video from {}: Video does not exist".format(playlist_name))
            return
        if video_id not in self._playlists[display_name]:
            print("Cannot remove video from {}: Video is not in playlist".format(playlist_name))
            return
        else:
            self._playlists[display_name].remove(video_id)
            print("Removed video from {}: {}".format(playlist_name, video.title))

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        display_name = playlist_name.lower()
        if display_name not in self._playlists:
            print("Cannot clear playlist {}: Playlist does not exist".format(playlist_name))
            return
        for video_id in self._playlists[display_name]:
            self._playlists[display_name].remove(video_id)
        print("Successfully removed all videos from {}".format(playlist_name))

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        display_name = playlist_name.lower()
        if display_name not in self._playlists:
            print("Cannot delete playlist {}: Playlist does not exist".format(playlist_name))
        else:
            self._playlists.pop(display_name, "not_found")
            print("Deleted playlist: {}".format(playlist_name))



    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        lower_search_term = search_term.lower()
        title_list = list(self._video_library.get_all_videos())
        title_list.sort(key=lambda x: x.title)
        for i in range(len(title_list)-1, -1, -1):
            video = title_list[i]
            if video._flag is True:
                title_list.remove(video)
        index_list = []
        for i in range(len(title_list)):
            current_title = title_list[i].title.lower()
            if lower_search_term in current_title:
                index_list.append(i)
        if len(index_list) == 0:
            print("No search results for {}".format(search_term))
            return
        print("Here are the results for {}:".format(search_term))
        options = []
        for i in range(len(index_list)):
            # video = title_list[index_list[i]]
            # tags = " ".join(video.tags)
            # print("{}) {} ({}) [{}]".format(video.title, video.video_id, tags))
            options.append(i+1)
            print("{}) {} ({}) [{}]".format(i+1, title_list[index_list[i]].title, title_list[index_list[i]].video_id,
                                            " ".join(title_list[index_list[i]].tags)))
        print("Would you like to play any of the above? If yes, specify the number of the video.")
        print("If your answer is not a valid number, we will assume it's a no.")
        try:
            ans = int(input())
        except ValueError:
            return
        if ans in options:
            self.play_video(title_list[index_list[ans-1]].video_id)


    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """

        if video_tag[0] != '#':
            print("No search results for {}".format(video_tag))
            return
        lower_video_tag = video_tag.lower()
        # title_list = self._video_library.get_all_videos()

        title_list = list(self._video_library.get_all_videos())
        title_list.sort(key=lambda x: x.title)
        for i in range(len(title_list)-1, -1, -1):
            video = title_list[i]
            if video._flag is True:
                title_list.remove(video)
        # title_list.sort(key=lambda x: x.title)
        index_list = []
        for i in range(len(title_list)):
            current_tags = title_list[i].tags
            for tag in current_tags:
                tag.lower()
            if video_tag in current_tags:
                index_list.append(i)
        if len(index_list) == 0:
            print("No search results for {}".format(video_tag))
            return
        print("Here are the results for {}:".format(video_tag))
        options = []
        for i in range(len(index_list)):
            # video = title_list[index_list[i]]
            # tags = " ".join(video.tags)
            # print("{}) {} ({}) [{}]".format(video.title, video.video_id, tags))
            options.append(i+1)
            print("{}) {} ({}) [{}]".format(i+1, title_list[index_list[i]].title, title_list[index_list[i]].video_id,
                                            " ".join(title_list[index_list[i]].tags)))
        print("Would you like to play any of the above? If yes, specify the number of the video.")
        print("If your answer is not a valid number, we will assume it's a no.")
        try:
            ans = int(input())
        except ValueError:
            return
        if ans in options:
            self.play_video(title_list[index_list[ans-1]].video_id)


    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """

        video = self._video_library.get_video(video_id)
        if not video:
            print("Cannot flag video: Video does not exist")
            return

        if video == self._current_video:
            self.stop_video()

        if video._flag:
            print("Cannot flag video: Video is already flagged")
            return

        video._flag = True
        video._flag_reason = flag_reason
        display_reason = flag_reason
        if flag_reason == "":
            display_reason = "Not supplied"
            video._flag_reason = "Not supplied"
        print("Successfully flagged video: {} (reason: {})".format(video.title, display_reason))




    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        video = self._video_library.get_video(video_id)
        if not video:
            print("Cannot remove flag from video: Video does not exist")
            return
        if not video._flag:
            print("Cannot remove flag from video: Video is not flagged")
            return 
        else:
            video._flag = None
            print("Successfully removed flag from video: {}".format(video.title))

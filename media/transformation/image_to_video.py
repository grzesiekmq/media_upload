import subprocess
import uuid

class ImageToVideoConverter():

    def transform(self, image_path, output_path):
        cmd = [
          "ffmpeg",
          "-loop", "1", "-i", image_path,
          "-t", "2", "-c:v", "libx264", "-preset", "ultrafast", "-pix_fmt", "yuv420p",
          output_path
        ]

        subprocess.call(cmd)

    def create_transition(self, image_from, image_to, output_path):
        cmd = [
          "ffmpeg",
          "-loop", "1", "-i", image_from,
          "-loop", "1", "-i", image_to,
          "-filter_complex", "[1:v][0:v]blend=all_expr='A*(if(gte(T,3),1,T/3))+B*(1-(if(gte(T,3),1,T/3)))'",
          "-t", "3", "-c:v", "libx264", "-preset", "ultrafast", "-pix_fmt", "yuv420p",
          output_path
        ]

        subprocess.call(cmd)

    def concat_videos(self, video_parts, output_path):

        tmp_file_list = "/tmp/videos_%s.txt" % str(uuid.uuid4())
        with open(tmp_file_list, "w+") as outf:
            outf.writelines(map(lambda x: "file '%s'\n" % x, video_parts))
            outf.close()

        cmd = [
          "ffmpeg",
          "-f", "concat", "-safe", "0",
          "-i", tmp_file_list,
          "-f", "mov", "-codec", "copy",
          "-shortest",
          output_path
        ]

        subprocess.call(cmd)
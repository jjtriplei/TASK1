import os
import config.settings as conf


def walk_folder(filepath):
    marked_files = []
    sample_files = []

    for root, dirs, files in os.walk(filepath):
        for filename in files:
            try:
                for file_type in conf.FILE_TYPES_TO_PROCESS:
                    file_extension = filename.split('.')[-1:][0]
                    if file_extension == file_type and "sample" not in filename.lower():
                        marked_files.append(os.path.join(root,filename))

                if "sample" in filename:
                  sample_files.append(os.path.join(root,filename))
            except TypeError:
                pass

    return (marked_files, sample_files)

def process_samples(samples):
    samples_to_return = []

    for sample in samples:
        if os.path.getsize(sample) > conf.FILE_SIZE_IN_MB * conf.MBS_IN_BYTES:
            samples_to_return.append(sample)

    return samples_to_return

def copy_file(source, destination):
    # shutil.copy2(marked_file, move_files_to_destination)
    pass

def move_file(source, destination):
    pass

def find_files_to_action():
    filenames_to_action = []

    for paths in conf.PATH_LIST:
        non_samples, sample = walk_folder(paths)
        processed_samples = process_samples(sample)
        filenames_to_action.append(non_samples + processed_samples)

    return filenames_to_action

if __name__ == '__main__':
    filename_list = find_files_to_action()
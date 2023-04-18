class FileHandler:
    def __init__(self, fname, verbose=True):
        self.fname = fname
        self.verbose = verbose
        self.threshold = 5000
        open(self.fname, 'a').close()

    @property
    def list(self):
        with open(self.fname, 'r') as f:
            lines = [x.strip('\n') for x in f.readlines()]
            return [x for x in lines if x]

    @property
    def set(self):
        data_lines = self.list
        if len(data_lines) > self.threshold:
            ld = len(data_lines)
            self.save_list(self.list[ld-self.threshold:])
        return set(self.list)

    def __iter__(self):
        for i in self.list:
            yield next(iter(i))

    def __len__(self):
        return len(self.list)

    def append(self, item, allow_duplicates=False):
        if self.verbose:
            msg = "Adding '{}' to `{}`.".format(item, self.fname)
            # print(msg)

        if not allow_duplicates and str(item) in self.list:
            msg = "'{}' already in `{}`.".format(item, self.fname)
            # print(msg)
            return

        with open(self.fname, 'a') as f:
            f.write('{item}\n'.format(item=item))

    def remove(self, x):
        x = str(x)
        items = self.list
        if x in items:
            items.remove(x)
            msg = "Removing '{}' from `{}`.".format(x, self.fname)
            # print(msg)
            self.save_list(items)

    def save_list(self, items):
        with open(self.fname, 'w') as f:
            for item in items:
                f.write('{item}\n'.format(item=item))

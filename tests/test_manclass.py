from App.apps import classNames as classy



class Test_class():
    def test_mark_data(self):
        assert(len(classy) == 6)
        assert classy == ['AbdomenCT', 'BreastMRI', 'ChestCT', 'CXR', 'Hand', 'HeadCT']
        assert type(classy) is list
        assert classy[0] == 'AbdomenCT'
        assert classy[1] == 'BreastMRI'
        assert classy[2] == 'ChestCT'
        assert classy[3] == 'CXR'
        assert classy[4] == 'Hand'
        assert classy[5] == 'HeadCT'
        assert 'HeadCT' in classy
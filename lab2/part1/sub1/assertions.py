class AssertThat:
    ID = 0

    def __init__(self, this):
        self.this = this
        self.id = AssertThat.ID
        AssertThat.ID += 1

    def __assert__(self, that, condition, message):
        assert condition, f"*this#{self.id} ({self.this}) {message} *that ({that})"
        return self

    def isLessThan(self, that):
        return self.__assert__(that, self.this < that, "should be less than")

    def isGreaterThan(self, that):
        return self.__assert__(that, self.this > that, "should be greater than")

    def isNotEqualTo(self, that):
        return self.__assert__(that, self.this < that, "should not be equal to")

    def andThat(self, this):
        return AssertThat(this)

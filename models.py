from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class DefenseSubmission(Base):
    __tablename__ = "defense_submissions"

    id: Mapped[int] = mapped_column(primary_key=True)
    image_url: Mapped[str] = mapped_column(nullable=False)
    kills: Mapped[int] = mapped_column(nullable=False)
    mentions: Mapped[list] = mapped_column(nullable=False)

    # points: Mapped["UserPoints"] = relationship(back_populates="submission")

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    handle: Mapped[str] = mapped_column(nullable=False)
    # points: Mapped["UserPoints"] = relationship(back_populates="user")

class UserPoints(Base):
    __tablename__ = "user_points"

    id: Mapped[int] = mapped_column(primary_key=True)
    points: Mapped[int] = mapped_column(nullable=False)
    # user: Mapped["User"] = relationship(back_populates="user")
    # submission: Mapped["DefenseSubmission"] = relationship(back_populates="points")



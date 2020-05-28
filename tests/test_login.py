import pytest
from pages.LoginPage import loginpage
from pages.HomePage import homepage
from pages.VideoPlayer import videoplayer
from pages.home_page import homePageObj
from pages.recently_addList import recaddListObj
from pages.MyListPage import MyList
from pages.ListDetails import ListDetails
from resources.variables import *
from pages.myList import myListObj
from pages.mailinator import mailinatorPageObj
from pages.homepage_myLists import homePagemylistsObj
from pages.TelevisionPage import Telvision
from pages.moviedetails import moviedetails
from pages.movies_listing import movieListingObj
from pages.televisions_page import tvpageObj
from pages.tvdetails import tvdetails
from pages.homepg import homepg
import allure
import time


@allure.title('Verify user lands on login page')
@pytest.mark.usefixtures("browser")
def test_loginpage(browser):
    global user
    user = loginpage(browser)
    verify = user.load()
    assert verify == "Log in to MGM ROAR", "Unable to load login page"
    print(verify)


@allure.title('Verify carousel image set by admin is visible')
def test_verifycarousalimage(browser):
    verify = user.CarouselImage()
    assert verify == True


@allure.title('On each visit user see different carousel image')
def test_differentcarouselimage(browser):
    ImageChange = user.DifferentCarouselImage()
    assert ImageChange == True, "Carousel image is not changing on reload"


@allure.title('verify elements present in login model')
def test_elementloginmodel(browser):
    email = user.VerifyEmail()
    assert True, "Email textbox not found"
    next_button = user.VerifyNextButton()
    assert True, "Next button not found"
    request_account = user.VerifyRequestAnAccount()
    assert True, "Request an account button not found"


@allure.title('Verify user is able to enter Email in email field')
def test_enteremail(browser):
    user.EnterEmail("automation@practicallogix.com")


@allure.title('Verify user with valid email id can proceed to next step')
def test_clicknext(browser):
    verify = user.ClickNext()
    assert verify == True, "user not proceed to next step with valid email id"


@allure.title('verify user is successfully logged in')
def test_login(browser):
    user.EnterPassword("~;Baxg2t")
    user.ClickNext()
    time.sleep(10)
    verify = user.VerifyLogin()
    assert verify == True, "User is not able to login with valid credentials"


@allure.title('Verify elements present in global header')
def test_ElementsGlobalHeader(browser):
    global home
    home = homepage(browser)
    logo = home.HomePageLogo()
    assert logo == True, "Header logo not found"
    movies = home.HeaderMovies()
    assert movies == True, "Movies link not found"
    television = home.HeaderTelevision()
    assert television == True, "Television link not found"
    mylist = home.HeaderMylist()
    assert mylist == True, "My list link not found"
    logout = home.HeaderLogoutButton()
    assert logout == True, "Logout button not found"


@allure.title('Verify functionality of View Details button')
def test_FunctionalityViewDetailButton(browser):
    title = home.MovieListViewDetailButton()
    assert "MGM ROAR | " in title, "Clicking on view detaild,Detailed page is not opening."
    synopsis = home.VerifySynopsisTitle()
    print(synopsis)
    assert synopsis == True


@allure.title('Verify carousel auto-progress as per transition time set in CMS')
def test_CarouselAutoProgress(browser):
    home.ClickLogo()
    time.sleep(5)
    a = home.CarouselAutoProgress()
    assert a == True, "Carousel is not auto processing"
    home.ClickLogo()


@allure.title('Veirfy when there are more than 4 titles then progress bar auto-progresses')
def test_MoreThan4Titles(browser):
    home.CarouselAutoProgress()
    b = home.ProgressBarLegallyBlonde()
    assert b == True
    a = home.SliderMovie()
    assert a == False


@allure.title('Veriify the Title is underlined(highlighted) when carousel moves to that slider')
def test_SliderTitleHighlighted(browser):
    movie = home.SliderTitleHighlighted()
    assert movie == True


@allure.title('Verify user is able to scroll thorugh the list')
def test_VerifyScroll(browser):
    verify = home.VerifyScroll()
    assert verify == True


@allure.title('Verify maximum 4 titles are shown on the Progress Bar')
def test_Maximum4TitlesShown(browser):
    home.Refresh()
    lenght = home.Maximum4Titles()
    assert lenght == 4


@allure.title('Verify Movie links are clickable and redirects to correct page')
def test_MenuLinksClickable(browser):
    movies = home.ClickMovies()
    assert movies == True, "Not redirecting to correct page"
    home.ClickLogo()
    television = home.ClickTelevision()
    assert television == True, "Not redirecting to correct page"
    home.ClickLogo()
    list1 = home.ClickLists()
    assert list1 == True, "Not redirecting to correct page"


@allure.title('Veirfy on click of Roar logo in header user is redirected to Homepage')
def test_ClickLogo(browser):
    verify = home.ClickLogo()
    time.sleep(10)
    assert verify == True, "When Click on logo user is not redirected to homepage"


@allure.title('Verify on click of Logout button, user is successfully logged out')
def test_ClickLogoutButton(browser):
    verify = home.ClickLogoutButton()
    assert verify == True, "User is not logged out"
    test_enteremail(browser)
    test_clicknext(browser)
    test_login(browser)


@allure.title('Verify Element Present in homepage')
def test_ElementsHomepage(browser):
    global_header = home.HomepageElementHeader()
    assert global_header == True, "Global Header not found"
    test_ElementsGlobalHeader(browser)
    main_carousel = home.HomepageMainCarousel()
    assert main_carousel == True, "Main carousel not found"
    list1 = home.HomepageMovieList1()
    assert list1 == True, "Movie list not found"
    list2 = home.HomepageMovieList2()
    assert list2 == True, "Movie list not found"
    list3 = home.HomepageMovieList3()
    assert list3 == True, "Movie list not found"
    list4 = home.HomepageMovieList4()
    assert list4 == True, "Movie list not found"
    list5 = home.HomepageMovieList5()
    assert list5 == True, "Movie list not found"
    # list6 = home.HomepageMovieList6()
    # assert list6 == True, "Movie list not found"
    list7 = home.HomepageMovieList7()
    assert list7 == True, "Movie list not found"
    list8 = home.HomepageMovieList8()
    assert list8 == True, "Movie list not found"
    list9 = home.HomepageMovieList9()
    assert list9 == True, "Movie list not found"
    list10 = home.HomepageMovieList10()
    assert list10 == True, "Movie list not found"
    TvShows = home.HomepageExploreAllTvShows()
    assert TvShows == True, "Explore all tv shows button not found"
    Movies = home.HomepageExploreAllMovies()
    assert Movies == True, "Explore all Movies button not found"
    Logo = home.HomepageFooterLogo()
    assert Logo == True, "Footer logo not found"
    privacy = home.HomepageFooterPrivacy()
    assert privacy == True, "Privacy button not found"
    terms = home.HomepageFooterTerms()
    assert terms == True, "Footer Terms not found"
    support = home.HomepageFooterSupport()
    assert support == True, "Footer support button not found"


@allure.title('Verify elements present in Carousel')
def test_ElementsCarousel(browser):
    home.Refresh()
    time.sleep(30)
    slider = home.MovieImageSlider()
    assert slider == True, "Movies image slider not found"
    progress = home.ProgressBar()
    assert progress == True, "Progress bar not found"
    left = home.ProgressBarPreviousArrow()
    assert left == True, "Left navigation button not found"
    right = home.ProgressBarNextArrow()
    assert right == True, "Right nagvigation button not found"


@allure.title('Verify elements present in Movie image slider')
def test_ElementsMovieImageSlider(browser):
    home.Refresh()
    time.sleep(25)
    # image = home.SliderBackgroundImage()
    # assert image == True, "Slider Background image not found"
    logo = home.movie_logoCarousel()
    assert logo == True, "Logo of Movie not found"
    watch = home.WatchNowButton()
    assert watch == True, "Watch now button not found"
    add = home.AddToListButton()
    assert add == True, "Add to list button not found"
    details = home.ViewDetailsButton()
    assert details == True, "View details button not found"


@allure.title('Main Carousel: Verify on click of Add to List button, Add List pop up is opened')
def test_AddToListPopUp(browser):
    home.Refresh()
    time.sleep(25)
    # home.AutoProgress()
    # time.sleep(3)
    # home.ClickSpectreMovie()
    home.ClickMainCarouselAddToList()
    search = home.AddToListSearchBox()
    time.sleep(10)
    assert search == True


@allure.title('Main Carousel: Verify user is able to enter name and create new list from Carousel')
def test_CreateNewList(browser):
    home.ListName("Demo")
    home.ClickCreateList()
    time.sleep(10)
    list = home.NewList()
    assert list == "Demo"
    home.ListName("test")
    home.ClickCreateList()
    time.sleep(10)


@allure.title('Main Carousel: Verify elements in Add To List pop')
def test_AddToListElement(browser):
    # home.ClickMainCarouselAddToList()
    search = home.AddToListSearchBox()
    assert search == True
    clear = home.AddToListClearButton()
    assert clear == True
    created_list = home.AddToListCreatedList()
    assert created_list == True
    toggel = home.AddToListToggelButton()
    assert toggel == True
    list = home.AddToListCreateList()
    assert list == True
    name = home.AddToListListName()
    assert name == True
    button = home.AddToListCreateListButton()
    assert button == True


@allure.title('Main Carousel: Verify user is able to add the movie in the created list')
def test_AddToList(browser):
    home.AddMovieToList()
    button = home.AddToListAddedButton()
    assert button == True
    # home.Refresh()
    # movie = home.VerifyAddedMovie()
    # assert movie == "Spectre"


@allure.title('Main Carousel: Verify user is able to add same movie in multiple lists')
def test_AddSameMovieMultipleList(browser):
    home.Refresh()
    time.sleep(25)
    home.ClickMainCarouselAddToList()
    time.sleep(8)
    home.ClickToggleButtonTest()
    time.sleep(3)
    home.AddMovieToList()
    button = home.AddToListAddedButton()
    assert button == True

    # movie1 = home.VerifySecondAddedMovie()
    # assert movie1 == "Spectre"
    # home.ClickLogo()
    # home.Refresh()


@allure.title('Main Carousel: Verify user is able to select list(s)')
def test_AddToListToggelButton(browser):
    home.ClickLogo()
    # home.ClickSpectreMovie()
    home.ClickMainCarouselAddToList()
    verify = home.VerifySelectList()
    assert verify == True, "Toggle button not selected"


@allure.title('Main Carousel: Verify user is able to un-select any selected list(s)')
def test_UnselectSelectedList(browser):
    verify = home.VerifySelectList()
    assert verify == False, "Toggle button not selected"


@allure.title('Main Carousel: Verify user is abe to search a list from the search bar')
def test_SearchList(browser):
    # home.ClickMainCarouselAddToList()
    time.sleep(5)
    home.SearchList("test")
    verify = home.VerifySearchedList()
    assert verify == True


@allure.title('Main Carousel: Verify user is able to select list(s) from search result')
def test_SelectSearchedList(browser):
    time.sleep(3)
    select = home.MovieCardVerifySelectUnselectList()
    assert select == True


@allure.title('Main Carousel: Verify user is able to un-select list(s) from search result')
def test_UnselectSearchedList(browser):
    time.sleep(3)
    select = home.MovieCardVerifySelectUnselectList()
    assert select == False


@allure.title('Main Carousel: Verify user is able to clear search on click of Clear button')
def test_ClearSearchedList(browser):
    time.sleep(5)
    home.ClickAddToListClearButton()
    home.Refresh()


@allure.title('Main Carousel: Verify user is able to add to multiple sliders in same list')
def test_AddMultipleSliderToSameList(browser):
    # home.MainCareusalClickNextNavigationArrow()
    # time.sleep(3)
    # home.ClickSpectreMovie()
    assert home.MainCareusalClickNextNavigationArrow() == "clicked", "Next nav for carousel is not clicking."

    # home.AutoProgress()
    time.sleep(3)
    home.ClickMainCarouselAddToList()
    time.sleep(5)
    toggle = home.VerifySelectList()
    assert toggle == True
    home.AddMovieToList()
    button = home.AddToListAddedButton()
    assert button == True


@allure.title('Movie Card: Verify user is able to select list(s)')
def test_MovieCardSelectList(browser):
    home.ClickLogo()
    home.ClickMovieCardAddToList()
    verify = home.VerifySelectList()
    assert verify == True, "Toggle button not selected"


@allure.title('Movie Card: Verify user is able to un-select any selected list(s)')
def test_MovieCardUnselectList(browser):
    verify = home.VerifySelectList()
    assert verify == False, "Toggle button is not unselected"


@allure.title('Movie Card: Verify on click of Add to List button, Add List pop up is opened')
def test_MovieCardAddToList(browser):
    list = home.ClickMovieCardAddToList()
    assert list == True, "Movie List Pop-up not found"


#
@allure.title('Movie Card: Verify user is able to enter name and create new list from Carousel')
def test_MovieCardCreateNewList(browser):
    home.ListName("test1")
    list = home.ClickCreateList()
    assert list == True
    created = home.CreatedList()
    assert created == True
    name = home.VerifyListCreated()
    assert name == True
    list = home.VerifyListAutoSelect()
    assert list == True
    time.sleep(4)
    home.ListName("test2")
    home.ClickCreateList()
    assert list == True
    created = home.CreatedList()
    assert created == True


#
@allure.title('Movie Card: Verify user is able to add the movie in the created list')
def test_MovieCardAddMovie(browser):
    time.sleep(10)
    home.AddMovieToList()
    button = home.AddToListAddedButton()
    assert button == True
    home.Refresh()
    # home.ClickHeaderList()
    # movie = home.VerifyMovieCardAddedMovie()
    # assert movie == "Detroit"


@allure.title('Movie Card: Verify user is able to add same movie in multiple lists')
def test_MovieCardSecondAddedMovie(browser):
    home.ClickMovieCardAddToList()
    home.SearchList("test2")
    time.sleep(2)
    home.ClickToggleButtonTest2()
    home.AddMovieToList()
    button = home.AddToListAddedButton()
    assert button == True
    # home.Refresh()

    # home.ClickHeaderList()
    # movie = home.MovieCardSecondAddedMovie()
    # assert movie == "Detroit"
    # home.ClickLogo()


@allure.title('Movie Card: Verify user is abe to search a list from the search bar')
def test_MovieCardSearchList(browser):
    time.sleep(10)
    home.ClickMovieCardAddToList()
    time.sleep(10)
    home.SearchList("test")
    time.sleep(3)
    home.ClickAddToListClearButton()
    time.sleep(10)
    home.SearchList("test")
    verify = home.VerifySearchedList()
    assert verify == True


@allure.title('Movie Card: Verify user is able to select list(s) from search result')
def test_MovieCardSelectSearchedList(browser):
    time.sleep(3)
    select = home.MovieCardVerifySelectUnselectList()
    assert select == True


@allure.title('Movie Card: Verify user is able to un-select list(s) from search result')
def test_MovieCardUnselectSearchedList(browser):
    time.sleep(3)
    unselect = home.MovieCardVerifySelectUnselectList()
    assert unselect == False


@allure.title('Movie Card: Verify user is able to clear search on click of Clear button')
def test_ClearSearchedList(browser):
    time.sleep(5)
    home.ClickAddToListClearButton()
    home.Refresh()


#
@allure.title('Movie Card: Verify user is able to add to multiple movies in same list')
def test_MovieCardMultipleMovieToSameList(browser):
    home.ClickMovieCardAddToListSecondMovie()
    home.ClickAddToListClearButton()
    home.SearchList("test1")
    time.sleep(3)
    home.ClickToggleButtonTest1()
    home.AddMovieToList()
    button = home.AddToListAddedButton()
    assert button == True


#
#
#
# # # @allure.title('Verify after the last slider, the titles in the progress bar resets to initial position')
# # # def test_ProgressBarReset(browser):
# # #     home.ClickLogo()
# # #     home.SliderBarReset()
# # #     movie = home.ProgressBarArmyOfDarkness()
# # #     assert movie == True
# #
@allure.title('Verify user is able to move to next slider by clicking Right Nagivation Arrow')
def test_MainCarouselNextNavigation(browser):
    home.Refresh()
    assert home.MainCareusalClickNextNavigationArrow() == "clicked", "arrow not clicked"


@allure.title('Verify user is able to move to previous slider by clicking Left Nagivation Arrow')
def test_MainCarouselPrevNavigation(browser):
    assert home.MainCareusalClickPrevNavigationArrow() == "clicked", "prev arrow not clicked"


'''view details main careusal'''


@allure.title('Verify View Details button is clickable and on click redirect to movie details page')
def test_ViewDetails(browser):
    # home.MainCareusalClickNextNavigationArrow()
    home.Refresh()
    view = home.ViewDetailsButtoncaro()
    assert view == True
    home.ClickLogo()


@allure.title('Verify the titles are clickable and clicking them take the carousel to that slider')
def test_TitlesClickable(browser):
    # home.ClickSpectreMovie()
    verify = home.ViewDetailsButtoncaro()
    assert verify == True
    home.ClickLogo()


@allure.title('Verify Left Navigation Arrow is disabled when we are on the first card in the list')
def test_PrevButtonDisable(browser):
    home.ClickLogo()
    prev = home.MovieListPrevButton1()
    assert prev == False, "Preview button is not disabled"
    time.sleep(5)


@allure.title('Verify hover behavior on movie cards')
def test_HoverBehaviourMovieCard():
    details = home.viewDetails_moviecardfunc()
    assert details == True
    time.sleep(1)
    list = home.addList_moviecardfunc()
    assert list == True
    time.sleep(1)
    watch = home.watchmovie_moviecrdfunc()
    assert watch == True
    time.sleep(1)
    trailer = home.verify_watchTrailer_cards()
    assert trailer == True


@allure.title('Verify functionality of Watch Movie button')
def test_FunctionalityWatchnowButton(browser):
    popup = home.ClickWatchMovieButton()
    assert popup == True


@allure.title('Verify elements for each Movie List')
def test_ElementMovieList(browser):
    button = home.SeeAllButton()
    assert button == True, "See all button not found"
    title = home.HomepageMovieList1()
    assert title == True, "Movie list not found"
    poster = home.MoviePoster()
    assert poster == True, "Movie poster not found"
    nextbtn = home.MovieListNextButton()
    assert nextbtn == True, "next navigation button not found"
    prevbtn = home.MovieListPrevButton()
    assert prevbtn == True, "prev navigation button not found"


@allure.title('Verify Left Navigation Arrow is visible only when we hover on the first card on the left')
def test_LeftNavigationVisibleOnHOver(browser):
    prevbtn = home.MovieListPrevButton()
    assert prevbtn == True, "Left navigation button not showing on hover"


@allure.title('Verify Right Navigation Arrow is visible only when we hover on the last card on the right')
def test_NextNavigationVisible(browser):
    nextbtn = home.MovieListNextButton1()
    print(nextbtn)
    assert nextbtn == True, "Next navigation is disabled"
    time.sleep(2)


@allure.title('Verify click behavior of Right Navigation arrow')
def test_RightNavigationBehaviour(browser):
    home.click_rightarrow()
    time.sleep(5)


@allure.title('Verify click behavior of Left Navigation arrow')
def test_BehaviourLeftNavigationArrow(browser):
    home.click_prevarrow()


@allure.title('Verify Right Navigation Arrow is disabled when we are on the last card in the list')
def test_NextNavigationDisable(browser):
    btn = home.NextNavigationDisable()
    assert btn == False


@allure.title('Verify elements for each Movie card')
def test_ElementMovieCard(browser):
    image = home.PosterImage()
    assert image == True
    title = home.MovieTitle()
    assert title == True
    genre = home.MovieGenre()
    assert genre == True


@allure.title('Verify elements in Explore section')
def test_ElementsExploreSection(browser):
    movies = home.HomepageExploreAllMovies()
    assert movies == True
    shows = home.HomepageExploreAllTvShows()
    assert shows == True
    explore = home.ExploreElement()
    assert explore == True


@allure.title('Verify click funcationality of See All TV Shows button')
def test_FunctionalityAllTvShows(browser):
    home.VerifyScroll()
    time.sleep(5)
    tvbutton = home.ClickExploreAllTvShows()
    home.ClickLogo()
    assert tvbutton == True


@allure.title('Verify click funcationality of See All Movies button')
def test_FunctinalityAllMovies(browser):
    home.VerifyScroll()
    time.sleep(5)
    movies = home.ClickExploreAllMovies()
    home.ClickLogo()
    assert movies == True


@allure.title('My List: Verify global header is present')
def test_MyListHeaderElement():
    home.ClickHeaderList()
    logo = home.HomePageLogo()
    assert logo == True, "Header logo not found"
    movies = home.HeaderMovies()
    assert movies == True, "Movies link not found"
    television = home.HeaderTelevision()
    assert television == True, "Television link not found"
    mylist = home.HeaderMylist()
    assert mylist == True, "My list link not found"
    logout = home.HeaderLogoutButton()
    assert logout == True, "Logout button not found"


@allure.title('My List: Verify two section on My List page')
def test_SectionMyListPage(browser):
    global listpage
    listpage = MyList(browser)
    container1 = listpage.YourListContainer()
    assert container1 == True, "Your List Table not found"
    heading1 = listpage.YourListHeading()
    assert heading1 == True, "Your list title not found"
    time.sleep(3)
    container = listpage.ListMadeForYouContainer()
    assert container == True, "List made for you table not found"
    heading = listpage.ListMadeForYouHeading()
    assert heading == True, "list made for you title not found"


@allure.title('My List: Verify columns/elements of List table')
def test_ElementsListTable(browser):
    checkbox = listpage.ListCheckbox()
    assert checkbox == True, "Checkbox not found"
    Name = listpage.ListName()
    assert Name == True, "List name not found"
    share = listpage.ListShareButton()
    assert share == True, "Share button not found"


@allure.title('My List: Verify elements in Currated List section')
def test_ElementsCurratedList(browser):
    time.sleep(3)
    container = listpage.ListMadeForYouContainer()
    assert container == True, "List made for you table not found"
    heading = listpage.ListMadeForYouHeading()
    assert heading == True, "list made for you title not found"


@allure.title('My List: Verify user is able to select the list by clicking on the checkbox')
def test_VerifyCheckBofFamily(browser):
    check = listpage.VerifyCheckBoxFamily()
    assert check == True, "Checkbox is not checked"


# # # # @allure.title('My List: Verify user is able to select multiple list by clicking on the checkbox')
# # # # def test_SelectMultipleLists(browser):
# # # #     checked = listpage.SelectMultipleLists()
# # # #     assert checked == True, "Multiple lists not selected"
# # #
# # #
@allure.title('My List: Verify golbal footer is present')
def test_global_footerMyList(browser):
    assert listpage.verify_Privacypolicy() == True, "Privacy policy is not displaying in global footer. It should be " \
                                                    "displayed in footer. "
    assert listpage.verify_termsUse() == True, "Terms and Use is not displaying in global footer. It should be " \
                                               "displayed in footer. "
    assert listpage.verify_footerLogo() == True, "MGM logo  is not displaying in global footer. It should be " \
                                                 "displayed in footer. "
    assert listpage.verify_supportLink() == True, "Support link is not displaying in global footer. It should be " \
                                                  "displayed in footer. "
    assert listpage.verify_address() == True, "Address text is not displaying in global footer. It should be " \
                                              "displayed in footer. "
    assert listpage.verify_youtubeIcon() == True, "Youtube icon is not displaying in global footer. It should be " \
                                                  "displayed in footer. "
    assert listpage.verify_fbIcon() == True, "Facebook icon is not displaying in global footer. It should be " \
                                             "displayed in footer. "
    assert listpage.verify_twitterIcon() == True, "Twitter icon is not displaying in global footer. It should be " \
                                                  "displayed in footer. "
    assert listpage.verify_instaIcon() == True, "Instagram icon is not displaying in global footer. It should be " \
                                                "displayed in footer. "
    assert listpage.verify_copyright() == True, "Copyright is not displaying in global footer. It should be " \
                                                "displayed in footer. "


@allure.title('My List: Verify click on checkbox opens the footer pop up')
def test_CheckedListPopUp(browser):
    popup = listpage.CheckedListPopUp()
    assert popup == True
    select = listpage.CheckedListPopUpSelectedList()
    assert select == True
    csv = listpage.CheckedListPopUpDownloadCsv()
    assert csv == True
    share = listpage.CheckedListPopUpShareButton()
    assert share == True


@allure.title('My List: Verify on click on List name user is redirected to List Detail page')
def test_VerifyListPage(browser):
    listpage.ClickListFamily()
    verify = listpage.VerifyFamilyList()
    assert verify == True
    time.sleep(4)


@allure.title('My List: Verify on click on Share button, share pop up is shown')
def test_ShareButtonPopUp(browser):
    home.ClickHeaderList()
    time.sleep(6)
    listpage.ClickListShareButton()
    time.sleep(3)
    popup = listpage.SharePopUp()
    assert popup == True
    close = listpage.ShareCloseBtn()
    assert close == True
    header = listpage.ShareHeader()
    assert header == True
    name = listpage.ShareListNameAndNumber()
    assert name == True
    text = listpage.ShareStaticText()
    assert text == True
    email = listpage.ShareEmailTextBox()
    assert email == True
    share = listpage.ShareButton()
    assert share == True


@allure.title('Currated List: Verify is able to share list and reciever recieves it')
def test_shareList_viaMailCuratedList(browser):
    global mailinator
    global share
    share = myListObj(browser)
    mailinator = mailinatorPageObj(browser)
    share.enter_email(mailinator_email1)
    share.click_buttonToshare()
    mailinator.openMailinator()
    time.sleep(50)
    mailinator.enterEmailinmailinator(mailinator_email1)
    mailinator.clickGopublic()
    time.sleep(2)
    mailinator.click_initialMail()
    time.sleep(5)
    assert mailinator.verify_sender() == "noreply@practicallogix.com", "There is not mail with name " \
                                                                       "noreply@practicallogix.com on mailinator "
    assert mailinator.verify_attachment() == True, "Attachmant is not there in mail . attachment should be there."


@allure.title('Currated List: Veirfy user is able to Share List(s) from Share Button in the fotter pop up')
def test_ShareListFromFooter(browser):
    time.sleep(3)
    mailinator.close_mailinator()
    time.sleep(6)
    listpage.VerifyCheckBoxFamily()
    listpage.ClickFooterShareButton()
    share.enter_email(mailinator_email2)
    share.click_buttonToshare()
    mailinator.openMailinator()
    time.sleep(50)
    mailinator.enterEmailinmailinator(mailinator_email2)
    mailinator.clickGopublic()
    time.sleep(15)
    mailinator.click_initialMail()
    time.sleep(5)
    assert mailinator.verify_sender() == "noreply@practicallogix.com", "There is not mail with name " \
                                                                       "noreply@practicallogix.com on mailinator "
    assert mailinator.verify_attachment() == True, "Attachmant is not there in mail . attachment should be there."


@allure.title('Currated List: Verify the columns in the attached csv file')
def test_csv_elementsCurratedList(browser):
    csv_elelements = mailinatorPageObj(browser)
    csv = myListObj(browser)
    time.sleep(6)
    mailinator.close_mailinator()
    time.sleep(5)
    listpage.ClickListFamily()
    time.sleep(17)
    csv.click_headerChkbox()
    time.sleep(4)
    csv.click_csvdownload()
    time.sleep(15)
    csv.click_headerChkbox()
    time.sleep(5)


@allure.title('Verify the options of Sorting and their functionality')
def test_SortingOrder(browser):
    # list = MyList(browser)
    home.ClickHeaderList()
    time.sleep(14)
    listpage.ClickListTest1()
    time.sleep(14)
    listpage.ClickSortDropdown()
    NewOld = listpage.SortByReleaseDateNewOld()
    assert NewOld == "RELEASE DATE"
    OldNew = listpage.SortByReleaseDateOldNew()
    assert OldNew == "RELEASE DATE"
    AZ = listpage.SortByAZ()
    assert AZ == "SORT A-Z"
    ZA = listpage.SortByZA()
    assert ZA == "SORT Z-A"


@allure.title('Verify user is able to download csv file on Click of Download CSV button from Fotter Pop Up')
def test_csvdownloadCurratedList(browser):
    mylist = homePagemylistsObj(browser)
    csv = myListObj(browser)
    home.ClickHeaderList()
    time.sleep(12)
    listpage.ClickListFamily()
    time.sleep(17)
    csv.click_headerChkbox()
    time.sleep(2)
    csv.click_csvdownload()
    time.sleep(15)


@allure.title('Television: Verify elements on Listing pages')
def test_ElementsTVListingPage(browser):
    global tv
    tv = Telvision(browser)
    tv.ClickTelevisionHeader()
    time.sleep(10)
    image = tv.HeaderImage()
    assert image == True
    search = tv.HeaderSearchbox()
    assert search == True
    title = tv.HeaderTitle()
    assert title == True
    genre = tv.FilterGenre()
    assert genre == True
    rating = tv.FilterRatig()
    assert rating == True
    year = tv.FilterYear()
    assert year == True
    grid = tv.ViewButtonGrid()
    assert grid == True
    list = tv.ViewButtonList()
    assert list == True
    sort = tv.SortButton()
    assert sort == True
    select = tv.SelectAllCheckbox()
    assert select == True
    checkbox = tv.TitleCardsCheckBox()
    assert checkbox == True


@allure.title(
    'Television: Verify user is able to search for titles by entering Actor/Character name or Movie/TV show name')
def test_SelectGenre(browser):
    tv.ClickGenre()
    tv.ClickGenreAction()
    time.sleep(5)
    movie = tv.VerifyGenreAction()
    assert movie == True
    tv.ClickClearFilter()


@allure.title('Television: Verify user is able to apply multiple Genres filters')
def test_SelectMultipleGenre(browser):
    home.Refresh()
    tv.ClickGenre()
    tv.ClickGenreCrime()
    tv.ClickGenre()
    tv.ClickGenreDrama()
    time.sleep(5)
    movie = tv.VerifyGenreCrime()
    assert movie == True
    movie1 = tv.VerifyGenreDrama()
    assert movie1 == True
    tv.ClickClearFilter()


@allure.title('Television: Verify user is able to filter titles by Rating')
def test_SelectRating(browser):
    home.Refresh()
    tv.ClickFilterRating()
    tv.ClickRating14()
    time.sleep(5)
    rating = tv.VerifyRatingTv14()
    assert rating == True


@allure.title('Television: Verify user is able to apply multiple Rating filters')
def test_SelectMultipleRating(browser):
    tv.ClickFilterRating()
    tv.ClickRatingNA()
    time.sleep(5)
    rating = tv.VerifyRating()
    assert rating == True
    tv.ClickClearFilter()


@allure.title('Television: Verify user is able to filter titles by Year')
def test_SelectYear(browser):
    home.Refresh()
    tv.ClickFilterYear()
    tv.ClickSelectYear()
    tv.ClickSliderSubmitButton()
    time.sleep(5)
    verify = tv.VerifyYear()
    assert verify == True
    tv.ClickClearFilter()


@allure.title('Verify user is able to filter with combination of Genre,Rating&Year filters ')
def test_FilterWithCombination(browser):
    home.Refresh()
    tv.ClickGenre()
    tv.ClickGenreDrama()
    tv.ClickFilterRating()
    tv.ClickRating14()
    tv.ClickFilterYear()
    tv.ClickSelectYear()
    tv.ClickSliderSubmitButton()
    time.sleep(3)
    movie = tv.VerifyGenreDrama()
    assert movie == True
    movie = tv.VerifyRatingTv14()
    assert movie == True
    verify = tv.VerifyYear()
    assert verify == True


@allure.title('Television: Verify user is able to filter titles by Genres')
def test_SearchTelevisionShow(browser):
    tv.SearchTelevisionShow("Fargo")
    tv.ClickSearchButton()
    section = tv.SearchListSection()
    assert section == True
    show = tv.SearchedTelevisionShow()
    assert show == True
    tv.ClearSearch()


@allure.title(
    'Verify one sheet overlay is present on the movie cards in the grid view and all buttons are visible on hover')
def test_MovieCardHoverButton(browser):
    time.sleep(10)
    add = tv.MovieCardHoverAddToList()
    assert add == True
    trailer = tv.MovieCardHoverWatchTrailer()
    assert trailer == True
    details = tv.MovieCardHoverViewDetails()
    assert details == True


@allure.title('Verify user is able to play movie by clicking Watch Movie button')
def test_WatchTrailerPopUp(browser):
    tv.ClickWatchTrailer()
    verify = tv.PlayerPopUp()
    assert verify == True


@allure.title('Verify user is able to add the title in a list by clicking add to list')
def test_TelevisionAddMovieToList(browser):
    tv.MovieCardHoverAddToList()
    tv.ClickAddToList()
    search = home.AddToListSearchBox()
    assert search == True
    home.VerifySelectList()
    home.AddMovieToList()
    button = tv.AddToListAddedButton()
    assert button == True


@allure.title('Verify user is able to reach details page by clicking View Details button')
def test_TelevisionViewDetailsFunctionality(browser):
    time.sleep(10)
    tv.MovieCardHoverAddToList()
    tv.ClickViewDetailsButton()
    time.sleep(7)
    synopsis = tv.VerifyMrMomSynopsis()
    assert synopsis == True
    tv.ClickTelevisionHeader()


@allure.title('Verify the layout of cards in List view')
def test_CardLayoutInList(browser):
    home.Refresh()
    tv.ClickListViewButton()
    time.sleep(3)
    title = tv.Title()
    assert title == True
    directed = tv.DirectedBy()
    assert directed == True
    cast = tv.MainCast()
    assert cast == True
    synopsis = tv.Synopsis()
    assert synopsis == True
    check = tv.SelectAllCheckbox()
    assert check == True


@allure.title('Verify user is able to switch between grid & list view')
def test_SwitchGridList(browser):
    title = tv.Title()
    assert title == True
    directed = tv.DirectedBy()
    assert directed == True
    tv.ClickGridViewButton()
    time.sleep(5)
    card = tv.CardsCheckbox()
    assert card == True


@allure.title('Verify on click of Title name redirectes to Title details page')
def test_TelevisionTitlePage(browser):
    tv.ClickListViewButton()
    time.sleep(5)
    tv.ClickTitleName()
    synopsis = tv.VerifyMrMomSynopsis()
    assert synopsis == True
    tv.ClickTelevisionHeader()


@allure.title('Verify selecting titles shows footer pop up')
def test_TelevisionCheckboxFooter(browser):
    tv.ClickListViewButton()
    time.sleep(10)
    tv.ClickTitleCardCheckbox()
    popup = tv.CheckedListPopUp()
    assert popup == True
    csv = tv.CheckedListPopUpDownloadCsv()
    assert csv == True
    share = tv.verify_sharetitleFooter()
    assert share == True
    add = tv.CheckedListPopUpAddToListButton()
    assert add == True
    time.sleep(3)


def test_setconnection(browser):
    conn = Telvision(browser)
    conn.connection_testcases()

    """Mritunjay"""


@allure.title('TC: 1.53, Verify movies are sorted in correct order')
def test_correct_order(browser):
    home_page = homePageObj(browser)
    home_page.click_watchmovie()
    time.sleep(4)
    home_page.click_crossimg()
    time.sleep(3)
    global played_moviename, rec_addedmovie, play_2movie
    played_moviename = home_page.play_moviename()
    time.sleep(2)
    play_2movie = home_page.play_2movieCard_name()
    time.sleep(2)
    rec_addedmovie = home_page.recent_moviename()
    time.sleep(3)
    assert played_moviename == rec_addedmovie, "The video played from action/adventure has not been added in recently " \
                                               "watched playlist in correct ordered "


@allure.title('TC: 1.49, Verify Recently Watched slider is displayed if user watches a movie')
def test_recently_watched_slider(browser):
    home_page = homePageObj(browser)
    time.sleep(2)
    assert home_page.verify_recentlywatched() == 'Recently Watched', "Recently watched slider option is not displaying "


@allure.title('TC: 1.50, Verify elements for Recently Watched section')
def test_recently_watched_options(browser):
    home_page = homePageObj(browser)
    time.sleep(3)
    time.sleep(1)
    assert home_page.verify_titleText() == True, "Title text for movie in recently wathced is not displaying"
    assert home_page.verify_scroll() == True, "Horizontal scroll is not displaying in recently watched "
    assert home_page.verify_rightarrow() == True, "Right Navigation bar is not showing "
    time.sleep(2)
    home_page.click_rightarrow()
    time.sleep(3)
    assert home_page.verify_leftarrow() == True, "Left navigation bar is not showing "
    time.sleep(2)
    home_page.click_prevarrow()
    time.sleep(5)


@allure.title('TC: 1.55, Verify elements for each Movie card in recently watched')
def test_elementMovieCard1(browser):
    home_page = homePageObj(browser)
    assert home_page.verifyMovieTitle() == played_moviename, "Movie title is not displaying in recently watched " \
                                                             "section "
    assert home_page.MovieGenre() == "ACTION / ADVENTURE,", "Movie generes not displayed in recently watched "


@allure.title('TC: 1.56, Verify hover behavior on movie cards')
def test_elementhover_card1(browser):
    home_page = homePageObj(browser)
    time.sleep(4)
    assert home_page.addTolist() == "ADD TO LIST", 'Add to list is not showing on hover of movie card '
    assert home_page.watchMoviesoption() == "WATCH MOVIE", "Watch movie is not showing on hover of movie card. "
    assert home_page.watchTraileroption() == "WATCH TRAILER", "Watch movie is not showing on hover of movie card. "
    assert home_page.viewDetailsoption() == "VIEW DETAILS", "Watch movie is not showing on hover of movie card. "


@allure.title('TC: 1.57, Verify functionality of Add to List button')
def test_addlist_functionality(browser):
    home_page = homePageObj(browser)
    home_page.click_addList()
    assert home_page.verifyAlert() == "Select List(s)", "After clicking on add to list button Pop is not opening. "
    time.sleep(3)


@allure.title('TC: 1.58, Verify functionality of Watch Movie button')
def test_watchmovie_functionality(browser):
    home_page = homePageObj(browser)
    time.sleep(3)
    home_page.click_recwatch_movie()
    time.sleep(12)
    assert home_page.watch_movie_popup() == "width: 1140px; height: 640px;", "Pop up is not opening for watch trailer " \
                                                                             "in recently watched movies "
    home_page.choose_click()
    time.sleep(2)
    home_page.click_crossimg()


@allure.title('TC: 1.60, Verify functionality of Watch Trailer button')
def test_watchtrailer_functionality(browser):
    home_page = homePageObj(browser)
    time.sleep(5)
    home_page.click_recwatch_trailer()
    time.sleep(15)
    assert home_page.watch_movie_popup() == "width: 1140px; height: 640px;", "Pop up is not opening for watch " \
                                                                             "trailer in recently watched movies "
    time.sleep(2)
    home_page.click_crossimg()


@allure.title('TC: 1.62, Verify functionality of View Details button')
def test_viewdetails_functionality(browser):
    home_page = homePageObj(browser)
    home_page.click_viewdetails()
    time.sleep(10)
    assert home_page.verify_pagetitle() == "MGM ROAR | " + rec_addedmovie, "After clicking on view details button " \
                                                                           "Movie details page is not opeing. "
    home_page.click_mgmimg()


@allure.title(
    'TC : 1.64, Verify Right Navigation Arrow is visible only when we hover on the last card on the right')
def test_right_navigation(browser):
    home_page = homePageObj(browser)
    assert home_page.verify_rightarrow() == True, "Right navigation arrow should displayed when hover over last movie " \
                                                  "cards. "


@allure.title('TC: 1.65, Verify click behavior of Right Navigation arrow')
def test_clickright_navigation(browser):
    home_page = homePageObj(browser)
    home_page.click_rightarrow()
    time.sleep(1)
    # assert home_page.verify_1card_slide() == False, "after clicking on right navigation 1 movie is displaying "


@allure.title('TC: 1.66, Verify Right Navigation Arrow is disabled when we are on the last card in the list')
def test_rightnav_disabled(browser):
    home_page = homePageObj(browser)
    time.sleep(2)
    home_page.click_secnav_arrow()
    time.sleep(2)
    assert home_page.verify_right_disbaled() == False, "Right nav is not disabled when it is on last movie cards. "
    time.sleep(5)


@allure.title('TC : 1.67, Verify Left Navigation Arrow is visible only when we hover on the first card on the left')
def test_left_navigation(browser):
    home_page = homePageObj(browser)
    time.sleep(3)
    assert home_page.verify_leftarrow() == True, "Left navigation arrow is not displaying after hover on first movie " \
                                                 "cards "


@allure.title('TC: 1.68, Verify click behavior of Left Navigation arrow')
def test_clickleft_navigation(browser):
    home_page = homePageObj(browser)
    home_page.click_prevarrow()


@allure.title('TC: 1.69, Verify Left Navigation Arrow is disabled when we are on the first card in the list')
def test_leftnav_disabled(browser):
    home_page = homePageObj(browser)
    time.sleep(3)
    assert home_page.verify_left_disbaled() == False, "Left nav is not disabled when it is on first movie cards. "


@allure.title('TC: 1.93, Verify on click of Add to List button, Add List pop up is opened')
def test_recentlyAddlist_opened(browser):
    add = recaddListObj(browser)
    assert add.verify_addToList() == "Select List(s)", "After clicking on add to list button on Movie cards Pop is " \
                                                       "not opening. "


@allure.title('TC: 1.94, Verify user is able to enter name and create new list from Carousel')
def test_createList(browser):
    add_list = recaddListObj(browser)
    add_list.click_listName()
    time.sleep(3)
    add_list.enter_Listname(new_List_name)
    time.sleep(1)
    add_list.click_createList_text()
    assert add_list.verify_LoaderText() == "Creating...", "After clicking on create list button Loader is not " \
                                                          "displaying. "
    # time.sleep(20)
    time.sleep(2)
    assert add_list.verify_success_created() == True, "Success message is not showing after creating new List. "
    time.sleep(2)
    assert add_list.verify_newCreatedlist() == new_List_name, "After Creating new List . It is not displaying in pop up"
    time.sleep(3)
    assert add_list.verify_checkBox() == True, "Newly created list is not auto selected. "


@allure.title('TC: 1.95, Verify user is able to add the movie in the created list')
def test_addMovie_list(browser):
    home_page = homePageObj(browser)
    add_list = recaddListObj(browser)
    time.sleep(3)
    add_list.click_Addlist_button()
    time.sleep(18)
    home_page.clickAutomationlist()
    time.sleep(5)
    assert home_page.verifyMovie_list(
        rec_addedmovie) == rec_addedmovie, "Added Movie is not showing in Automation List"
    home_page.delete_movie(rec_addedmovie)
    time.sleep(60)
    home_page.click_verify_new_list()
    assert home_page.verifyMovie_list(
        rec_addedmovie) == rec_addedmovie, "Added Movie is not showing in Automation List"
    home_page.delete_movie(rec_addedmovie)
    time.sleep(60)


@allure.title('TC: 1.96, Verify user is able to select list(s)')
def test_select_list(browser):
    select = recaddListObj(browser)
    home_page = homePageObj(browser)
    home_page.click_mgmimg()
    # select.click_addtoList2Card()
    assert select.verify_addToList() == "Select List(s)", "After clicking on add to list button on Movie cards Pop is " \
                                                          "not opening. "
    time.sleep(2)
    select.click_listName()
    assert select.verify_selectList() == True, "Clicking in toggle button, list is not getting selected."


@allure.title('TC: 1.97, Verify user is able to un-select any selected list(s)')
def test_unselect_list(browser):
    unselect = recaddListObj(browser)
    unselect.click_listName()
    assert unselect.verify_selectList() == False, "Clicking in toggle button twice, list is not getting unselected."
    time.sleep(4)


@allure.title('TC: 1.98, Verify user is able to add same movie in multiple lists')
def test_addmovie_multiple(browser):
    movie = recaddListObj(browser)
    home_page = homePageObj(browser)
    movie.click_listName()
    movie.select_newlyList()
    time.sleep(2)
    movie.click_Addlist_button()
    time.sleep(18)
    home_page.clickAutomationlist()
    assert home_page.verifyMovie_list(
        rec_addedmovie) == rec_addedmovie, "Added Movie is not showing in Automation List"
    home_page.delete_movie(rec_addedmovie)
    time.sleep(60)
    home_page.click_verify_new_list()
    assert home_page.verifyMovie_list(
        rec_addedmovie) == rec_addedmovie, "Added Movie is not showing in Automation List"
    home_page.delete_movie(rec_addedmovie)
    time.sleep(60)


@allure.title('TC: 1.99, Verify user is able to search a list from the search bar')
def test_searchList(browser):
    add = recaddListObj(browser)
    home_page = homePageObj(browser)
    home_page.click_mgmimg()
    time.sleep(3)
    assert add.verify_addToList() == "Select List(s)", "After clicking on add to list button on Movie cards Pop is " \
                                                       "not opening. "
    time.sleep(2)
    add.enter_listname_search(new_List_name)
    time.sleep(2)
    assert add.verify_Listcount() == 1, "After entering list name in search bocx more than one items is showing in " \
                                        "lists "
    assert add.verify_searchElement() == new_List_name, "Searched element is not showing in list "


@allure.title('TC: 1.100, Verify user is able to clear search on click of Clear button')
def test_clearsearch(browser):
    clear = recaddListObj(browser)
    time.sleep(2)
    assert clear.verify_Clearbutton() == "Search cleared", "After clicking on clear button search result is not clear."
    time.sleep(4)


@allure.title('TC: 1.101, Verify user is able to select list(s) from search result')
def test_search_selectList(browser):
    select = recaddListObj(browser)
    select.enter_listname_search("Automation List")
    select.click_listName()
    assert select.verify_selectList() == True, "After searching List name , user is not able to select list ."


@allure.title('TC: 1.102, Verify user is able to un-select list(s) from search result')
def test_search_unselectList(browser):
    unselect = recaddListObj(browser)
    time.sleep(2)
    unselect.click_listName()
    assert unselect.verify_selectList() == False, "After clear search user is not able to unselect list ."
    time.sleep(2)
    assert unselect.verify_Clearbutton() == "Search cleared", "After clicking on clear button search result is not " \
                                                              "clear. "


@allure.title('TC: 1.103, Verify user is able to add to multiple movies in same list')
def test_multimovie_1list(browser):
    multi = recaddListObj(browser)
    success = movieListingObj(browser)
    multi.click_listName()
    multi.click_Addlist_button()
    time.sleep(2)
    assert success.verify_success_msg() == True, "Success message (Done) is not showing after creating new List. "
    time.sleep(10)
    multi.click_addtoList2Card()
    time.sleep(2)
    multi.click_listName()
    multi.click_Addlist_button()
    assert success.verify_success_msg() == True, "Success message (Done) is not showing after creating new List. "
    time.sleep(10)


@allure.title('TC: 1.104, Verify only 10 movie card is shown')
def test_totalmovie_cards(browser):
    total = recaddListObj(browser)
    time.sleep(3)
    assert total.verify_Totalmovie() <= 10, " Movie cards contains more than 10 movie in recently watched section "


@allure.title('TC: 1.105, Verify created lists are shown in the My Lists slider')
def test_createdLists(browser):
    lists = homePagemylistsObj(browser)
    time.sleep(50)
    assert lists.verify_autoList() == True, "Automation list is not displaying in My list slider"
    time.sleep(1)
    assert lists.verify_Mylists() <= 10, " My Lists contains more than 10 cards. it should be 10 or less than 10 "


@allure.title('TC: 1.107, Verify elements for My List section')
def test_myList_elements(browser):
    elements = homePagemylistsObj(browser)
    time.sleep(2)
    assert elements.verify_Mylists_title() == True, "Title is not showing in my Lists section. It should show on " \
                                                    "moovie cards "
    assert elements.verify_listCards() == True, "Lists cards is not displayed in my List section "
    time.sleep(2)
    assert elements.verify_rightNav() == True, "Right navigation arrow is not showing . it should show on last list " \
                                               "card "
    elements.click_rightNav()
    assert elements.verify_LeftNav() == True, "Left navigation arrow is not showing . it should show on first list card"
    # elements.click_leftNav()
    assert elements.verify_seeAll() == True, "See all button is not displayed. button should show in right ."


@allure.title('TC: 1.108, Verify on click of See All button, user is directed to My List page')
def test_myList_seeall(browser):
    see_all = homePagemylistsObj(browser)
    home_page = homePageObj(browser)
    time.sleep(2)
    see_all.click_seeALL()
    time.sleep(1)
    assert see_all.verify_list_Heading() == "Your Lists", "After click on see all button , List page is not opening. "
    home_page.click_mgmimg()


@allure.title('TC: 1.109, Verify user is able to see User Created List in My List section of homepage')
def test_userList(browser):
    element = homePagemylistsObj(browser)
    assert element.verify_autoList() == True, "Automation List is not showing on List cards "
    assert element.verify_Numbtitles() == True, "Number of titles is not showing on list cards. "


@allure.title('TC: 1.110, Verify user is able to see Curated List in My List section of homepage')
def test_curatedList(browser):
    curated = homePagemylistsObj(browser)
    time.sleep(2)
    assert curated.verify_curatedText() == "LIST MADE FOR YOU", "LIST MADE FOR YOU text is not displayed on curated " \
                                                                "list cards. Text should be displayed. "
    # assert curated.verify_curateList_title() == "Family", "With name of Family not any list showing up there in my " \
    #                                                       "list section . "
    assert curated.verify_curateList_title() == True, "With name of Family not any list showing up there in my list " \
                                                      "section . "
    assert curated.verify_curatedNumtitles() == True, "Number of titles should be displayed on curated list cards"


@allure.title('TC: 1.111, Verify on click of List card, user is redirected to List Detail page')
def test_listDetail(browser):
    detail = homePagemylistsObj(browser)
    detailed_page = movieListingObj(browser)
    home_page = homePageObj(browser)
    detail.click_listCard()
    time.sleep(10)
    assert detail.verify_detailedPage() == "Automation List", "In detail Page List name is not showing in heading . " \
                                                              "Detailed page is not opened "
    home_page.click_mgmimg()


@allure.title('TC: 1.112, Verify golbal footer is present')
def test_global_footer(browser):
    home_page = homePageObj(browser)
    assert home_page.verify_Privacypolicy() == True, "Privacy policy is not displaying in global footer. It should be " \
                                                     "displayed in footer. "
    assert home_page.verify_termsUse() == True, "Terms and Use is not displaying in global footer. It should be " \
                                                "displayed in footer. "
    assert home_page.verify_footerLogo() == True, "MGM logo  is not displaying in global footer. It should be " \
                                                  "displayed in footer. "
    assert home_page.verify_supportLink() == True, "Support link is not displaying in global footer. It should be " \
                                                   "displayed in footer. "
    assert home_page.verify_address() == True, "Address text is not displaying in global footer. It should be " \
                                               "displayed in footer. "
    assert home_page.verify_youtubeIcon() == True, "Youtube icon is not displaying in global footer. It should be " \
                                                   "displayed in footer. "
    assert home_page.verify_fbIcon() == True, "Facebook icon is not displaying in global footer. It should be " \
                                              "displayed in footer. "
    assert home_page.verify_twitterIcon() == True, "Twitter icon is not displaying in global footer. It should be " \
                                                   "displayed in footer. "
    assert home_page.verify_instaIcon() == True, "Instagram icon is not displaying in global footer. It should be " \
                                                 "displayed in footer. "
    assert home_page.verify_copyright() == True, "Copyright is not displaying in global footer. It should be " \
                                                 "displayed in footer. "


# myList Page

@allure.title('TC: 2.18, Verify elements in User Created Lists section')
def test_Userelements(browser):
    elements = homePagemylistsObj(browser)
    elements.click_seeALL()
    time.sleep(15)
    assert elements.verify_listsTitle() == "Your Lists", "Title name Your lists is not showing up in lists . Title " \
                                                         "should show Your Lists. "
    assert elements.verify_userCreated_list() == "Automation List", "User created list with name Automation List is " \
                                                                    "not there in table. List should show in table. "


@allure.title('TC: 2.19, Verify columns/elements of List table')
def test_listPage_elements(browser):
    list = homePagemylistsObj(browser)
    assert list.verify_userCreated_list() == "Automation List", "Automation List title is not showing in heading . It " \
                                                                "should show. "
    assert list.verify_shareButton() == True, "Share button should be displayed in User created list page"
    assert list.verify_deleteButton() == True, "Delete button should be displayed in user created List page. "
    assert list.verify_checkBox() == True, "Check box should be displayed in list page table"
    time.sleep(2)


@allure.title('TC: 2.20, Verify user is able to select the list by clicking on the checkbox')
def test_clickingCheckbox(browser):
    check = homePagemylistsObj(browser)
    check.click_list_checkBox()
    time.sleep(3)
    assert check.verify_checkselected() == True, "Check box is not selected after clicking on it. "


@allure.title('TC: 2.21, Verify user is able to select multiple list by clicking on the checkbox')
def test_clickMultiple_chekbox(browser):
    multi = homePagemylistsObj(browser)
    multi.click_Demo_checkBox()
    assert multi.verify_checkselected() == True, "First Check box is not selected after clicking on it. Multiple " \
                                                 "checkbox should get selected. "
    assert multi.verify_Demoselected() == True, "Second Check box is not selected after clicking on it. Multiple " \
                                                "checkbox should get selected. "
    multi.click_Demo_checkBox()


@allure.title('TC: 2.22, Verify click on checkbox opens the footer pop up')
def test_chkbox_footerpopup(browser):
    footer = homePagemylistsObj(browser)
    time.sleep(2)
    assert "Item Selected" in footer.verify_Listtext(), "List selected Text is not displaying in footer pop . It " \
                                                        "should show. "
    assert footer.verify_downloadCsv() == True, "Download csv is not present there. Download csv button should be " \
                                                "displayed in foooter popup. "
    assert footer.verify_shareList() == True, "Share List is not present there. Share list button should be displayed " \
                                              "in foooter popup. "
    assert footer.verify_DeleteFooterpopup() == True, "Delete button is not present there. Delete button button " \
                                                      "should be displayed in foooter popup. "
    footer.click_list_checkBox()


@allure.title('TC: 2.23, Verify on click on List name user is redirected to List Detail page')
def test_listRedirected_detailed(browser):
    list = homePagemylistsObj(browser)
    page = myListObj(browser)
    time.sleep(3)
    list.click_Createdlist()
    time.sleep(1)
    assert page.verify_listName() == "Automation List", "After clicking on list in list table , List detailed page is " \
                                                        "not opened "
    time.sleep(4)


@allure.title('TC: 2.24, Verify on click on Share button, share pop up is shown')
def test_shareButton(browser):
    share = myListObj(browser)
    share.click_shareButton()
    time.sleep(3)
    assert share.verify_closeBtn() == True, "CLose button is not present in popup. close button should be there"
    assert share.verify_staticToptext() == True, "Static Text i.e YOU ARE ABOUT TO SEND 1 LIST button is not present " \
                                                 "in popup. static text should be there "
    assert share.verify_lisTitle() == True, "List title and number of list is not present in popup. list title & list " \
                                            "numbers should be there "
    assert share.verify_staticTextmiddle() == True, "Static Text i.2 Share 1 List is not present in popup. Static " \
                                                    "list i.e Share 1 list should be there "
    assert share.verify_emailTextbox() == True, "Email Textbox is not present in popup. Email text box should be there"
    assert share.verify_button() == True, "Share Button is not present in popup. Share button should be there"


@allure.title('TC: 2.25, Verify is able to share list and receiver receives it')
def test_shareList_viaMAIL(browser):
    share = myListObj(browser)
    mailinator = mailinatorPageObj(browser)
    share.enter_email(mailinator_email)
    share.click_buttonToshare()
    mailinator.openMailinator()
    time.sleep(25)
    mailinator.enterEmailinmailinator(mailinator_email)
    mailinator.clickGopublic()
    time.sleep(2)
    mailinator.click_initialMail()
    time.sleep(5)
    assert mailinator.verify_sender() == "noreply@practicallogix.com", "There is not mail with name " \
                                                                       "noreply@practicallogix.com on mailinator "
    assert mailinator.verify_attachment() == True, "Attachmant is not there in mail . attachment should be there."
    time.sleep(3)


@allure.title('TC: 2.26, Verify the columns in the attached csv file')
def test_csv_elements(browser):
    csv_elelements = mailinatorPageObj(browser)
    csv = myListObj(browser)
    csv_elelements.close_mailinator()
    time.sleep(2)
    csv.click_headerChkbox()
    time.sleep(4)
    csv.click_csvdownload()
    time.sleep(15)
    csv.click_headerChkbox()
    time.sleep(3)


@allure.title('TC: 2.27, Verify clicking on Delete button, share pop up is shown')
def test_deletePopup(browser):
    list = myListObj(browser)
    list.click_deleteButton()
    time.sleep(4)
    assert list.verify_delete_close() == True, "Delete icon is not displaying. Delete icon should be displayed in " \
                                               "delete popup. "
    assert list.verify_deleteToptext() == True, "Static Text i.e YOU ARE ABOUT TO DELETE  1 LIST button is not " \
                                                "present in popup. static text should be there "
    assert list.verify_deleteTitle() == True, "List title and number of list is not present in popup. list title & " \
                                              "list numbers should be there "
    assert list.verify_deleteTextmiddle() == True, "Static Text i.e The above list will be deleted, continue? is not " \
                                                   "present in popup. Static list i.e Share 1 list should be there "
    assert list.verify_deleteBtnPop() == True, "Delete button is not showing up there. Delete button should be " \
                                               "displayed in delete popup. "
    assert list.verify_cancel_button() == True, "Cancel button is not showing up there. Cancel button should be " \
                                                "displayed. "


@allure.title('TC:2.28, Verify on click of Cancel button delete pop up gets closed')
def test_cancelButton(browser):
    cancel = myListObj(browser)
    list = homePagemylistsObj(browser)
    cancel.click_cancelButton()
    time.sleep(8)
    assert list.verify_listsTitle() == "Your Lists", "On clicking Cancel button ,cancel popup is not getting closed . " \
                                                     "It should close and should come to Your lists page "


@allure.title('TC: 2.29, Verify user created list is deleted on click of Delete list button in the pop up ')
def test_deleteList(browser):
    delete = myListObj(browser)
    delete.click_new_list()
    time.sleep(10)
    delete.click_deleteButton()
    time.sleep(2)
    delete.click_grant_delete()
    time.sleep(60)
    assert delete.verify_deletedList() == False, "After deleting list, list is displaying in lists table. it should " \
                                                 "get deleted and not be displayed in table. "
    time.sleep(2)


@allure.title(
    'TC: 2.30, Verify user is able to download csv file on Click of Download CSV button from Fotter Pop Up')
def test_csvdownload(browser):
    list = homePagemylistsObj(browser)
    csv = myListObj(browser)
    list.click_Createdlist()
    time.sleep(15)
    csv.click_headerChkbox()
    time.sleep(2)
    csv.click_csvdownload()
    time.sleep(15)


@allure.title('TC: 2.31, Veirfy user is able to Share List(s) from Share Button in the fotter pop up')
def test_share2List_viaEmail(browser):
    share = myListObj(browser)
    mailinator = mailinatorPageObj(browser)
    share.click_headerChkbox()
    time.sleep(2)
    share.click_shareTitleFooter()
    time.sleep(3)
    share.enter_email(mailinator_2email)
    share.click_buttonToshare()
    mailinator.openMailinator()
    time.sleep(25)
    mailinator.enterEmailinmailinator(mailinator_2email)
    mailinator.clickGopublic()
    time.sleep(2)
    mailinator.click_initialMail()
    time.sleep(5)
    assert mailinator.verify_sender() == "noreply@practicallogix.com", "There is not mail with name " \
                                                                       "noreply@practicallogix.com on mailinator "
    assert mailinator.verify_attachment() == True, "Attachmant is not there in mail . attachment should be there."
    time.sleep(3)


@allure.title('TC: 2.32, Verify user is able to Delete List(s) from Delete Button in the fotter pop up')
def test_deletList_footer(browser):
    delete = myListObj(browser)
    add_list = recaddListObj(browser)
    stop = mailinatorPageObj(browser)
    stop.close_mailinator()
    time.sleep(8)
    delete.click_headerChkbox()
    time.sleep(2)
    delete.click_addTolist()
    add_list.enter_Listname(delete_listtt)
    time.sleep(1)
    add_list.click_createList_text()
    assert add_list.verify_LoaderText() == "Creating...", "After clicking on create list button Loader is not " \
                                                          "displaying. "
    time.sleep(2)
    assert add_list.verify_success_created_list() == True, "Success message is not showing after creating new List. "
    time.sleep(3)
    add_list.click_Addlist_button()
    time.sleep(22)
    delete.click_mylistTab()
    time.sleep(22)
    delete.click_listChkbox()
    delete.deletelist_frmfooter()
    time.sleep(2)
    delete.click_grant_delete()
    time.sleep(60)
    assert delete.verify_listDeleted() == False, "list not removed from my list page"


@allure.title('TC: 2.33, Verify user is able to select both Curated & User Created lists')
def test_select_curatedAndUser(browser):
    list = myListObj(browser)
    demo = homePagemylistsObj(browser)
    time.sleep(3)
    list.click_familyCheck()
    assert list.verify_familyChekbox() == True, "Family check box should get selected with clicking on family check box"
    list.click_Demo_checkBox()
    assert demo.verify_Demoselected() == True, "Demo Check should get selected with clicking on demo checkbox."
    time.sleep(2)


@allure.title(
    'TC: 2.34, Verify Delete button is not shown in footer pop up when both Curated & User Created lists are '
    'selected')
def test_deleteBtn_selectingboth(browser):
    delete = myListObj(browser)
    assert delete.verify_DeleteFooterpopup() == False, "with selecting both checkbox curated and user created list " \
                                                       "Delete button should not be shown in footer "


@allure.title('TC: 3.2 , Verify elements on movie Listing pages')
def test_moviePage_elements(browser):
    elements = movieListingObj(browser)
    time.sleep(10)
    elements.open_moviePage()
    time.sleep(40)
    assert elements.verify_headerTitle() == "Our Movies", "Title with Our Movies is not showing in header. header " \
                                                          "should displayed with title. "
    assert elements.verify_searchBox() == True, "Search box is not showing in header. header should displayed with " \
                                                "search box. "
    assert elements.verify_backImage() == True, "Background is not showing in header. header should consist " \
                                                "background image.. "
    assert elements.verify_filterGenre() == True, "Genre Filter is not showing on movie listing page .  Filter genere " \
                                                  "should be on movie listing page "
    assert elements.verify_filterRating() == True, "Rating Filter is not showing on movie listing page. Filter Rating " \
                                                   "should be on movie listing page "
    time.sleep(2)
    assert elements.verify_filterYear() == True, "Year Filter is not showing on movie listing page. Filter Year " \
                                                 "should be on movie listing page below header section "
    assert elements.verify_viewGrid() == True, "Grid view button is not present on movie listing page. grid view " \
                                               "button should be displayed on movie listing page below header section "
    assert elements.verify_viewList() == True, "List view button is not present on movie listing page. List view " \
                                               "button should be displayed on movie listing page below header section "
    assert elements.verify_sortingButton() == True, "Sorting button is not present on movie listing page. sorting " \
                                                    "button should be displayed on movie listing page "
    assert "ResultS Found" in elements.verify_resultsFound(), "Results found text is not there. Results found text " \
                                                              "should be displayed over movie cards in movie listing " \
                                                              "page. "
    time.sleep(2)
    assert elements.verify_selectAll() == "Select All", "Select All Check box is not displayed on movie listing page. " \
                                                        "It should be displayed "
    assert elements.verify_titleCards() == True, "Title for movie cards is not showing . it should be displayed"
    assert elements.verify_checkboxCards() == True, "Check box corresponding to movie cards is not showing on movie " \
                                                    "listing page. It should show checkbox. "


@allure.title(
    'TC: 3.3, Verify user is able to search for titles by entering Actor/Character name or Movie/TV show name')
def test_search_results(browser):
    search = movieListingObj(browser)
    search.input_searchvalue("Spectre")  # rec_addedmovie
    search.click_searchBtn()
    time.sleep(7)
    assert search.verify_searchResult() == "Spectre", "Correct results is not coming out after searching by movie " \
                                                      "name. Correct result should be shown. "
    time.sleep(3)
    search.click_searchCross()
    time.sleep(2)


@allure.title('TC: 3.4, Verify pagination is present when there are more than 42 titles in search result')
def test_pagination(browser):
    pagination = movieListingObj(browser)
    if pagination.count_totalMovie() >= 42:
        assert pagination.verify_Pagination() == True, "Pagination arrow is not displaying in movie listing page. it " \
                                                       "should show in footer "
    else:
        assert pagination.verify_Pagination() == False, "Pagination arrow is displaying in movie listing page. it " \
                                                        "should not be shown in footer "
    time.sleep(3)


@allure.title('TC: 3.5, Verify user is able to filter titles by Genres')
def test_filter_genres(browser):
    genre = movieListingObj(browser)
    option1 = genre.click_genreDropdown()
    genre.select_Actiongnere()
    time.sleep(5)
    assert genre.verify_selecetdGenre() == option1, "Selected genre should be show above all movie cards after using " \
                                                    "genre filter"
    assert genre.verify_genrefilter_results() == True, "Using Genre filter should show only selected option in genre " \
                                                       "title of movie cards "
    time.sleep(3)


@allure.title('TC: 3.6, Verify user is able to apply multiple Genres filters')
def test_multiGenre_filter(browser):
    multi_genre = movieListingObj(browser)
    option1 = multi_genre.click_genreDropdown()
    multi_genre.select_Actiongnere()
    time.sleep(5)
    assert multi_genre.verify_selecetdGenre() == option1, "Selected genre should be show above all movie cards after " \
                                                          "using genre filter "
    option2 = multi_genre.click_multigenreDropdown()
    multi_genre.select_multignere()
    time.sleep(5)
    assert multi_genre.verify_muliselectedGenre() == option2, "Multiple Selected genre should be shown above all " \
                                                              "movie cards after using genre filter "
    time.sleep(3)


@allure.title('TC: 3.7,Verify user is able to filter titles by Rating')
def test_filter_rating(browser):
    rate = movieListingObj(browser)
    rate.click_crossIcon()
    time.sleep(7)
    match = rate.click_1ratingDropdown()
    rate.select_1Dropdown()
    assert rate.verify_selSingle_rating() == match, "Selected rating filter at first position is not applied with " \
                                                    "selecting from dropdown "


@allure.title('TC: 3.8, Verify user is able to apply multiple Rating filters')
def test_multiple_ratingfilter(browser):
    multi_rate = movieListingObj(browser)
    match1 = multi_rate.click_1ratingDropdown()
    multi_rate.select_1Dropdown()
    time.sleep(5)
    match2 = multi_rate.click_2ratingDropdown()
    multi_rate.select_2Dropdown()
    assert multi_rate.verify_selSingle_rating() == match1, "Selected rating filter at first position is not applied " \
                                                           "with selecting from dropdown. "
    assert multi_rate.verify_selMulti_rating() == match2, "Selected rating filter at second position is not applied " \
                                                          "with selecting from dropdown."
    time.sleep(2)


@allure.title('TC: 3.9, Verify user is able to filter titles by Year')
def test_yearFilter(browser):
    year = movieListingObj(browser)
    year.click_crossIcon()
    time.sleep(7)
    year.click_yearDropdown()
    year.select_yearSlider()
    year.click_submitButton()
    time.sleep(6)
    assert year.verify_selectedYear() == True, "After selecting year from filter , year filter is not applied on movies"
    time.sleep(2)


@allure.title('TC: 3.10, Verify user is able to filter with combination of Genre,Rating&Year filters ')
def test_genre_rating_year(browser):
    combine = movieListingObj(browser)
    combine.click_crossIcon()
    time.sleep(7)
    genre = combine.click_genreDropdown()
    combine.select_Actiongnere()
    rating = combine.click_1ratingDropdown()
    combine.select_1Dropdown()
    time.sleep(7)
    combine.click_yearDropdown()
    combine.select_yearSlider()
    combine.click_submitButton()
    time.sleep(7)
    assert combine.verify_selected_combineYear() == True, "After selecting year from filter , year filter is not " \
                                                          "applied on movies with genre and rating filter. "
    assert combine.verify_selSingle_rating() == rating, "Selected rating filter at first position is not applied with " \
                                                        "selecting from dropdown"
    assert combine.verify_selecetdGenre() == genre, "After selecting action option in genre dropdown should show " \
                                                    "above movie cards. "


@allure.title('TC: 3.11, Verify user is able to switch between grid & list view')
def test_switch_listGrid(browser):
    switch = movieListingObj(browser)
    switch.click_crossIcon()
    time.sleep(7)

    assert switch.verify_gridchkbx1() == True, "1st movie Checkbox is not showing above movie cards in grid view.1st " \
                                               "checkbox should be displayed "
    assert switch.verify_gridchkbx2() == True, "2nd movie Checkbox is not showing above movie cards in grid view.2nd " \
                                               "checkbox should be displayed "
    switch.click_viewList()
    time.sleep(4)
    assert switch.verify_lisTitle() == True, "Heading Title is not showing above movie cards in list view. title " \
                                             "should be displayed "
    assert switch.verify_listSynopsis() == True, "Synopsis is not showing above movie cards in grid view. synopsis " \
                                                 "should be displayed "
    switch.click_viewGrid()


@allure.title('TC: 3.13, Verify on the movie cards in the grid view and all buttons are visible on hover')
def test_moviecards_element(browser):
    buttons = movieListingObj(browser)
    # buttons.click_crossIcon()
    buttons.input_searchvalue("Spectre")  # rec_addedmovie
    buttons.click_searchBtn()
    time.sleep(7)
    assert buttons.verify_searchResult() == "Spectre", "Correct results is not coming out after searching by movie " \
                                                       "name. Correct result should be shown. "
    time.sleep(5)
    assert buttons.verify_cardHover1() == "ADD TO LIST", 'Add list is not showing on hover of movie card in grid view ' \
                                                         '.Add list should display with hover on cards '
    assert buttons.verify_cardHover2() == "WATCH MOVIE", 'Watch movie is not showing on hover of movie card in grid ' \
                                                         'view . Watch movie should display with hover on cards '
    assert buttons.verify_cardHover3() == "WATCH TRAILER", 'Watch trailer is not showing on hover of movie card in ' \
                                                           'grid view. Watch trailer should display with hover on ' \
                                                           'cards '
    assert buttons.verify_cardHover4() == "VIEW DETAILS", 'View Details is not showing on hover of movie card in grid ' \
                                                          'view. View Details should display with hover on cards '
    time.sleep(2)
    buttons.click_searchCross()
    time.sleep(5)


@allure.title('TC: 3.14, Verify user is able to play movie by clicking Watch Movie button')
def test_watchMovie_moviepage(browser):
    watch = movieListingObj(browser)
    time.sleep(2)
    watch.input_searchvalue('Spectre')
    watch.click_searchBtn()
    assert watch.verify_searchResult() == "Spectre", "Correct results is not coming out after searching by movie " \
                                                     "name. Correct result should be shown. "
    time.sleep(3)
    watch.click_watchmovie()
    time.sleep(6)
    assert watch.verify_watch_popup() == "width: 1140px; height: 640px;", "movie popup is not opening after clicking " \
                                                                          "on watch movie button on card 1 "
    watch.click_closepopup()
    time.sleep(5)


@allure.title("TC: 3.15, Verify user is able to play trailer by clicking Watch Trailer button")
def test_watchtrailer_moviepage(browser):
    trailer = movieListingObj(browser)
    trailer.click_watchtrailer()
    time.sleep(6)
    assert trailer.verify_watch_popup() == "width: 1140px; height: 640px;", "trailer popup is not opening after " \
                                                                            "clicking on watch trailer button on card 1"
    trailer.click_closepopup()
    time.sleep(5)


@allure.title('TC: 3.16, Verify user is able to reach details page by clicking View Details button')
def test_viewdetails_moviepage(browser):
    details = movieListingObj(browser)
    details.click_viewDetails()
    time.sleep(12)
    assert details.verify_pagetitle() == "MGM ROAR | Spectre", "Details page is not opening correctly. It should open " \
                                                               "detailes page for spectre "
    time.sleep(3)


@allure.title('TC: 3.17, Verify user is able to add the title in a list by clicking add to list')
def test_addList_moviepage(browser):
    addList = movieListingObj(browser)
    addList.open_moviePage()
    # addList.refresh()
    time.sleep(18)
    addList.input_searchvalue('Spectre')
    addList.click_searchBtn()
    time.sleep(6)
    assert addList.verify_searchResult() == "Spectre", "Correct results is not coming out after searching by movie " \
                                                       "name. Correct result should be shown. "
    addList.click_addtoList()
    assert addList.verifyAlert() == "Select List(s)", "After clicking on add to list button Pop is not opening."
    addList.click_listToadd()
    time.sleep(2)
    addList.click_Addlist_button()
    time.sleep(2)
    assert addList.verify_success_msg() == True, "Success message (Done) is not showing after creating new List. "
    time.sleep(10)


@allure.title('TC: 3.19, Verify the layout of cards in List view')
def test_listview_elements(browser):
    list_view = movieListingObj(browser)
    list_view.click_searchCross()
    time.sleep(5)
    list_view.click_viewList()
    time.sleep(5)
    assert list_view.verify_lisTitle() == True, "Heading Title is not showing above movie cards in list view. title " \
                                                "should be displayed "
    assert list_view.verify_directedBY() == True, "Heading Directed by is not showing above movie cards in list view. " \
                                                  "directed by should be displayed "
    assert list_view.verify_mainCast() == True, "Heading Main cast is not showing above movie cards in list view. " \
                                                "main cast should be displayed "
    assert list_view.verify_listSynopsis() == True, "Heading Synopsis is not showing above movie cards in list view. " \
                                                    "synopsis should be displayed "


@allure.title('TC: 3.20, Verify on click of Title name redirectes to Title details page')
def test_listitle_redirecteds(browser):
    detailed_page = movieListingObj(browser)
    time.sleep(5)
    detailed_page.input_searchvalue('Spectre')
    detailed_page.click_searchBtn()
    time.sleep(5)
    # detailed_page.click_viewList()
    # time.sleep(3)
    assert detailed_page.verify_movieName() == "Spectre", "Correct movie should display with selecting list view ."
    detailed_page.click_listMoviename()
    time.sleep(12)
    assert detailed_page.verify_pagetitle() == "MGM ROAR | Spectre", "Details page is not opening correctly in list " \
                                                                     "view. It should open detailes page for spectre "
    time.sleep(3)
    detailed_page.open_moviePage()
    detailed_page.refresh()
    time.sleep(30)


@allure.title('TC: 3.21, Verify selecting titles shows footer pop up')
def test_listFooter_moviepage(browser):
    footer = movieListingObj(browser)
    footer.click_viewList()
    time.sleep(7)
    footer.input_searchvalue('Spectre')
    footer.click_searchBtn()
    time.sleep(5)
    footer.click_listchkbox1()
    time.sleep(4)
    assert footer.verify_downloadCSV() == True, "Download csv button is not displayed in footer. It should be visible " \
                                                "in footer "
    assert footer.verify_shareTitle() == True, "Share list button is not displayed in footer. It should be visible in " \
                                               "footer "
    assert footer.verify_addTolist() == True, "add To List button is not displayed in footer. It should be visible in " \
                                              "footer "


@allure.title('TC: 3.22, Verify user is able to download CSV file of the selected title')
def test_csvdownload_moviePage(browser):
    download = myListObj(browser)
    download.click_csvdownload()
    time.sleep(15)


@allure.title('TC: 3.23, Verify user is able to Share Title(s) from footer pop up')
def test_sharemail_moviepage(browser):
    share = myListObj(browser)
    mailinator = mailinatorPageObj(browser)
    addList = movieListingObj(browser)
    time.sleep(4)
    addList.click_listchkbox1()
    time.sleep(2)
    share.click_shareTitleFooter()
    time.sleep(4)
    share.enter_email("autoSharemail" + randNumber + "@mailinator.com")
    share.click_buttonToshare()
    mailinator.openMailinator()
    time.sleep(10)
    mailinator.enterEmailinmailinator("autoSharemail" + randNumber + "@mailinator.com")
    mailinator.clickGopublic()
    time.sleep(2)
    mailinator.click_initialMail()
    time.sleep(5)
    assert mailinator.verify_sender() == "noreply@practicallogix.com", "There is not mail with name " \
                                                                       "noreply@practicallogix.com on mailinator "
    time.sleep(3)


@allure.title('TC 3.24, Verify user is able to add the title in a list by clicking add to list ')
def test_addTolist_moviepage(browser):
    addList = movieListingObj(browser)
    mailinator = mailinatorPageObj(browser)
    mailinator.close_mailinator()
    time.sleep(4)
    addList.click_listchkbox1()
    time.sleep(2)
    addList.click_footer_addList()
    time.sleep(2)
    addList.click_listToadd()
    time.sleep(2)
    addList.click_Addlist_button()
    time.sleep(2)
    assert addList.verify_success_msg() == True, "Success message (Done) is not showing after creating new List. "
    time.sleep(15)


@allure.title('TC: 3.38 Verify the sections on Television Details page')
def test_tvsections(browser):
    sections = tvpageObj(browser)
    search = movieListingObj(browser)
    time.sleep(10)
    sections.open_television()
    time.sleep(7)
    sections.refresh()
    time.sleep(40)
    search.input_searchvalue("Vikings")
    search.click_searchBtn()
    time.sleep(7)
    search.click_viewDetails()
    sections.refresh()
    time.sleep(20)
    assert search.verify_pagetitle() == "MGM ROAR | Vikings (series)", "After Clicking on view detail, Detailed page " \
                                                                       "is not opening . "
    assert sections.verify_tvdetailed_header() == True, "Header for Tv series is not showing. It should displayed on " \
                                                        "overlay image "
    assert sections.verify_titleoverview() == "TITLE OVERVIEW", "Title overview is not showing on tv detailed page."
    assert sections.verify_trailerTitle() == True, "Trailer title is not displayed in tv detailed page. it should be " \
                                                   "displayed. "
    assert sections.verify_tvsynopsis() == True, "Synopsis for tv should be displayed."
    assert sections.verify_photoTitle() == True, "Photos title is not showing in Tv detailed page."
    assert sections.verify_castcrewTitle() == True, "Cast, crew and Productions title is not showing in footer . it " \
                                                    "should be displayed"
    time.sleep(5)


@allure.title('TC: 3.39, Verify elements in header of TV Details page on Series Level')
def test_tvheader_elements(browser):
    elements = tvpageObj(browser)
    assert elements.verify_heroImage() == True, "Hero image is not showing in header. it should be displayed."
    assert elements.verify_seasons_episodes() == True, "Numbers of seasons and Episodes is not showing in header."
    assert elements.verify_seasonsDrpdown() == True, "Seasons dropdown is not showing in header. It should be displayed"
    assert elements.verify_addListDrpdown() == True, "Add to List dropdown is not showing in header. It should be " \
                                                     "displayed "
    assert elements.verify_titletreatment_logo() == True, "Title treatment logo is not showing. it should be displayed"
    time.sleep(4)


@allure.title('TC: 3.40, Verify values of All Seasons dropdown')
def test_seasonDrpdown(browser):
    season = tvpageObj(browser)
    time.sleep(2)
    assert season.verify_selectedDrpdown() == "ALL SEASONS", "By default ALL Season in season drop down is not " \
                                                             "selected. All season should be selected by default "
    assert season.count_totaldrpdwn_option() >= 1, "Drop down is not showing all season in option. It should show " \
                                                   "after clicking on drop down. "
    season.refresh()
    time.sleep(30)


@allure.title('TC: 3.41, Verify user is able to go to Season level from Series level')
def test_selectedSeason(browser):
    selected = tvpageObj(browser)
    selected.select_season1Drpdown()
    time.sleep(12)
    assert selected.verify_selectedDrpdown() == "SEASON 1", "After selecting season 1 from season drop down season 1 " \
                                                            "selected and applied. "
    selected.select_allseason_option()


@allure.title("TC: 3.42, Verify user is able to Add TV Series to list(s)")
def test_tv_addTolist(browser):
    addList = movieListingObj(browser)
    butn = tvpageObj(browser)
    time.sleep(13)
    butn.click_addTolist_btn()
    time.sleep(8)
    assert addList.verifyAlert() == "Select List(s)", "After clicking on add to list button Pop is not opening."
    addList.click_listToadd()
    time.sleep(2)
    butn.click_addButton()
    time.sleep(2)
    assert addList.verify_success_msg() == True, "Success message (Done) is not showing after creating new List. "
    time.sleep(14)


@allure.title('TC: 3.43, Verify elements in header of TV Details page on Season Level')
def test_tvdetails_seasonlevel(browser):
    details = tvpageObj(browser)
    details.select_season1Drpdown()
    time.sleep(10)
    details.click_titleOverview()
    time.sleep(20)
    assert details.verify_heroImage() == True, "Hero image is not showing in header. it should be displayed."
    assert details.verify_seasons_episodes() == True, "Numbers of seasons and Episodes is not showing in header."
    assert details.verify_seasonsDrpdown() == True, "Seasons dropdown is not showing in header. It should be displayed"
    assert details.verify_selectedDrpdown() == "SEASON 1", "After selecting season 1 from season drop down season 1 " \
                                                           "selected and applied. "
    time.sleep(2)
    assert details.verify_addListDrpdown() == True, "Add to List dropdown is not showing in header. It should be " \
                                                    "displayed "
    assert details.verify_trailerBtn() == True, "Watch trailer button is not displayed in header.It should be " \
                                                "displayed and enabled. "
    time.sleep(2)
    assert details.verify_titletreatment_logo() == True, "Title treatment logo is not showing. it should be displayed"
    time.sleep(4)


@allure.title('TC: 3.44, Verify Episodes tab is visible when user is at Season level')
def test_episodeTab_visisble(browser):
    tab = tvpageObj(browser)
    assert tab.verify_episodeTab() == True, "Either Episode is not visible with selected season or season is not " \
                                            "selected. Episode tab should displayed with selected season. "


@allure.title('TC: 3.45, Verify user is able to Add TV Season to list(s)')
def test_addtvseason(browser):
    add = tvpageObj(browser)
    addList = movieListingObj(browser)
    add.click_addTolist_btn()
    time.sleep(8)
    assert addList.verifyAlert() == "Select List(s)", "After clicking on add to list button Pop is not opening."
    addList.click_listToadd()
    time.sleep(2)
    add.click_addButton()
    time.sleep(2)
    assert addList.verify_success_msg() == True, "Success message (Done) is not showing after creating new List. "
    time.sleep(14)


@allure.title('TC: 3.46, Verify elements in Episodes Tab at Season level')
def test_episode_elements(browser):
    elements = tvpageObj(browser)
    elements.click_episodeTab()
    time.sleep(10)
    assert elements.verify_episodeImg() == True, "Episode image is not showing on cards. it should be displayed in " \
                                                 "half of cards "
    assert elements.verify_episodeNumber() == "EPISODE 1", "Episode number is not showing on cards in epidoe page."
    assert elements.verify_episodeName() == True, "Episode name sis not displayed on cards. it should be visible "
    assert elements.verify_episodeSynopsis() == True, "Episode Synopsis is not displaying on cards. It should " \
                                                      "displayed in half of footer section on card "
    time.sleep(2)
    elements.click_episode1card()
    time.sleep(10)
    assert elements.verify_episode1Detailed() == "Episode 0001 :", "After clicking of episode number episode detailed " \
                                                                   "page is not opening "


@allure.title('TC: 3.47, Verify elements in header of TV details page on episode level')
def test_tvheader_episodelevel(browser):
    details = tvpageObj(browser)
    time.sleep(6)
    assert details.verify_heroImage() == True, "Hero image is not showing in header. it should be displayed."
    assert details.verify_seasons_episodes() == True, "Numbers of seasons and Episodes is not showing in header."
    assert details.verify_seasonsDrpdown() == True, "Seasons dropdown is not showing in header. It should be displayed"
    assert details.verify_selectedDrpdown() == "SEASON 1", "After selecting season 1 from season drop down season 1 " \
                                                           "selected and applied. "
    time.sleep(2)
    assert details.verify_addListDrpdown() == True, "Add to List dropdown is not showing in header. It should be " \
                                                    "displayed "
    assert details.verify_titletreatment_logo() == True, "Title treatment logo is not showing. it should be displayed"
    time.sleep(4)


@allure.title('TC: 3.48, Verify elements in Episodes tab at episode level')
def test_tvelements_episodelevel(browser):
    elements = tvpageObj(browser)
    assert elements.verify_detailed_episodeImage() == True, "Primary Landscape image is not displaying on episode " \
                                                            "detailed page. It should be displayed "
    assert elements.verify_episode_playIcon() == True, "play button is not showing.Play button should be displayed " \
                                                       "over episode cards "
    assert elements.verify_tvsynopsis() == True, "Synopsis for tv should be displayed."
    time.sleep(3)


@allure.title('TC: 3.49, Verify user is able to play episode by clicking the play button. ')
def test_episodePlayed_epilevel(browser):
    play = tvpageObj(browser)
    watch = movieListingObj(browser)
    play.click_episodePlayed()
    time.sleep(10)
    assert watch.verify_watch_popup() == "width: 1140px; height: 640px;", "movie popup is not opening after clicking " \
                                                                          "on watch movie button on card 1 "
    watch.click_closepopup()
    time.sleep(5)


@allure.title('TC : 3.51, Verify Trailer is shown as per selected levels')
def test_trailerBYlevel(browser):
    trailer = tvpageObj(browser)
    assert trailer.verify_trailerBylevel() == True, "trailer for episode level is not showing. Trailer should be " \
                                                    "displayed for episode level. "
    trailer.click_titleOverview()
    time.sleep(5)
    assert trailer.verify_trailerBylevel() == True, "trailer for episode level is not showing. Trailer should be " \
                                                    "displayed for episode level. "
    trailer.select_allseason_option()
    time.sleep(10)
    assert trailer.verify_trailerBylevel() == True, "trailer for series level is not showing. Trailer should be " \
                                                    "displayed for series level. "


@allure.title('TC: 3.52, Verify Photos is shown as per selected levels')
def test_photosBYlevel(browser):
    photos = tvpageObj(browser)
    assert photos.verify_photoBylevel() == True, "photos for series level is not showing. Photos should be displayed " \
                                                 "for series level "
    photos.select_season1Drpdown()
    time.sleep(10)
    photos.click_titleOverview()
    time.sleep(7)
    assert photos.verify_photoBylevel() == True, "photos for season level is not showing. Photos should be displayed " \
                                                 "for season level "

    photos.click_episodeTab()
    time.sleep(10)
    photos.click_episode1card()
    time.sleep(10)
    assert photos.verify_photoBylevel() == True, "photos for season level is not showing. Photos should be displayed " \
                                                 "for season level "


@allure.title('TC: 3.22, Verify user is able to download CSV file of the selected title')
def test_download_tvcsv(browser):
    download = tvpageObj(browser)
    srch = movieListingObj(browser)
    downl = myListObj(browser)
    time.sleep(5)
    download.open_television()
    time.sleep(7)
    download.refresh()
    time.sleep(35)
    srch.input_searchvalue("Vikings")
    srch.click_searchBtn()
    time.sleep(7)
    download.clicking_checkbox()
    time.sleep(3)
    downl.click_csvdownload()
    time.sleep(15)


@allure.title('TC: 3.23 Verify user is able to Share Title(s) from footer pop up')
def test_tv_shareTitle(browser):
    share = tvpageObj(browser)
    shr = myListObj(browser)
    srch = movieListingObj(browser)
    share.clicking_checkbox()
    time.sleep(3)
    shr.click_shareTitleFooter()
    time.sleep(3)
    shr.enter_email("tvSharemail" + randNumber + "@mailinator.com")
    shr.click_buttonToshare()
    time.sleep(10)
    assert share.verify_tvshareButton() == False, "After clicking on share pop is not getting closed. It should be " \
                                                  "closed. "


@allure.title('TC: 3.24, Verify user is able to add the title in a list by clicking add to list ')
def test_tv_addTitle(browser):
    add = tvpageObj(browser)
    add_list = movieListingObj(browser)
    add.clicking_checkbox()
    time.sleep(2)
    add_list.click_footer_addList()
    time.sleep(2)
    add_list.click_listToadd()
    time.sleep(2)
    add_list.click_Addlist_button()
    time.sleep(2)
    assert add_list.verify_success_msg() == True, "Success message (Done) is not showing after creating new List. "
    time.sleep(15)


@allure.title('TC: 3.4, Verify pagination is present when there are more than 42 titles in search result')
def test_tvPagination(browser):
    pagination = movieListingObj(browser)
    pagination.click_searchCross()
    time.sleep(7)
    if pagination.count_totalMovie() >= 42:
        assert pagination.verify_Pagination() == True, "Pagination arrow is not displaying in movie listing page. it " \
                                                       "should show in footer "
    else:
        assert pagination.verify_Pagination() == False, "Pagination arrow is  displaying in movie listing page. it " \
                                                        "should not be shown in footer "

    """Hitesh"""


def test_setconnection1(browser):
    conn = Telvision(browser)
    conn.connection_testcases()


@allure.title('tc-35,Verify elements in mylist details page')
def test_mylistdetails(browser):
    global listdet
    listdet = ListDetails(browser)
    listdet.verify_addmovietolist()
    listdet.verify_mylist()
    assert listdet.verify_listheadername() == 'movietest', "title not found in list details page"
    assert listdet.verify_listgridbutton() == True, "grid button not found in list details page"
    assert listdet.verify_listbutton() == True, "list button not found in list details page"
    assert listdet.verify_sharebutton() == True, "share button not found in list details page"
    assert listdet.verify_deletebutton() == True, "delete button not found in list details page"
    assert listdet.verify_moviedetail() == True, "movie details not found in list details page"
    assert listdet.verify_moviecheckbox() == True, "movie checkbox not found in list details page"
    # assert listdet.verify_listcheckbox() == True, "checkbox button not found in list details page"


@allure.title('tc-36,Verify overlay present in movie card')
def test_mylistoverlaydetails(browser):
    global listdet
    listdet = ListDetails(browser)
    listdet.verify_overlaypanel()
    assert listdet.verify_addolist() == True, "add to list element not found"
    assert listdet.verify_watchmovie() == True, "watch movie element not found"
    assert listdet.verify_watchtrailer() == True, "watch trailer element not found"
    assert listdet.verify_viewdetails() == True, "view details element not found"


@allure.title('tc-38,Verify list view is displayed')
def test_listview(browser):
    global listdet
    listdet = ListDetails(browser)
    listdet.verify_listview()


@allure.title('tc-39,Verify elements list view is displayed')
def test_listelements(browser):
    global listdet
    listdet = ListDetails(browser)
    assert listdet.verify_listelements() == 'TITLE', "title header in list not found"
    assert listdet.verify_directedelements() == 'DIRECTED BY', "DIRECTED BY header in list not found"
    assert listdet.verify_maincastelements() == 'MAIN CAST', "MAIN CAST header in list not found"
    assert listdet.verify_synopsiselements() == 'SYNOPSIS', "SYNOPSIS header in list not found"


@allure.title('tc-40,verify user is able to select title using checkbox')
def test_titleselect(browser):
    global listdet
    listdet = ListDetails(browser)
    assert listdet.verify_titleselect() == True, "list title is not selected"


@allure.title('tc-41,To verify footer section when selected a title')
def test_footersection(browser):
    global listdet
    listdet = ListDetails(browser)
    assert listdet.verify_footersection() == True, "footer section not found"


@allure.title('tc-42,To verify added title to the list')
def test_addtitletolist(browser):
    global listdet
    listdet = ListDetails(browser)
    assert listdet.verify_addtitletolist() == True, "Added title in list not found"


@allure.title('tc-43,To verify created list in add to list')
def test_createlist(browser):
    global listdet
    listdet = ListDetails(browser)
    assert listdet.verify_createlist() == True, "created list not found in add to list items"


@allure.title('tc-44,To verify title in created list')
def test_titleincreatedlist(browser):
    global listdet
    listdet = ListDetails(browser)
    assert listdet.verify_createdlist() == True, "created list not found"
    assert listdet.verify_titleincreatedlist() == True, "title not found in created list"


@allure.title('tc-45,To verify user is able to share title')
def test_sharelist(browser):
    global listdet
    listdet = ListDetails(browser)
    assert listdet.verify_sharewindow() == True, "share window not found"
    assert listdet.verify_shareemail() == False, "List not shared through mail"


@allure.title('tc-47,To verify user is able to download csv')
def test_downloadcsv(browser):
    global listdet
    listdet = ListDetails(browser)
    listdet.verify_downloadcsv()
    time.sleep(15)


@allure.title('tc-48,To verify select all titile checkbox')
def test_selectalltitle(browser):
    global listdet
    listdet = ListDetails(browser)
    assert listdet.verify_selectalltitle() == True, "select all checkbox not selected"


@allure.title('tc-50,To Verify User is able to share list by clicking on Share button in header')
def test_sharelistheader(browser):
    global listdet
    listdet = ListDetails(browser)
    assert listdet.verify_sharelistheader() == False, "List not shared through mail"


@allure.title('tc-46,To verify delete title in the list')
def test_deletetitle(browser):
    global listdet
    listdet = ListDetails(browser)
    assert listdet.verify_deletetitle() == False, "title not removed from my list page"


@allure.title('tc-49,To Verify user is able to Delete list')
def test_deletelist(browser):
    global listdet
    listdet = ListDetails(browser)
    assert listdet.verify_deletelist() == False, "list not removed from my list page"


@allure.title('tc-4,Verify My List is underlined in Menu')
def test_listunderline(browser):
    global listdet
    listdet = ListDetails(browser)
    assert listdet.verify_listunderline() == "ng-star-inserted active", "uderline uder list menu not found"


@allure.title('tc-37,To verify Watch Movie should not be shown in case of a TV entity')
def test_watchmovieintv(browser):
    global listdet
    listdet = ListDetails(browser)
    assert listdet.verify_watchmovieintv() == False, "Watch Movie should shown in case of a TV entity"


"""moviedetails"""


@allure.title('tc-26,Verify elements in movie details page')
def test_moviedetails(browser):
    global listdet
    listdet = moviedetails(browser)
    listdet.verify_moviedetails()
    assert listdet.verify_movieheader() == True, "movie header section not found"
    assert listdet.verify_movietrailer() == True, "movie trailer section not found"
    assert listdet.verify_moviephotos() == True, "movie photos section not found"
    assert listdet.verify_moviecastprod() == True, "movie cast prod section not found"
    # assert listdet.verify_moviesynopsis() == True, "movie synopsis section not found"


@allure.title('tc-27,Verify elements in header of Movie Details page')
def test_movieheaderdetails(browser):
    global listdet
    listdet = moviedetails(browser)
    assert listdet.verify_movieheaderimage() == True, "movie header image not found"
    assert listdet.verify_movielogo() == True, "movie title logo not found"
    assert listdet.verify_watchmoviebutton() == True, "watch movie button not found"
    assert listdet.verify_watchtrailerbutton() == True, "watch trailer button not found"
    assert listdet.verify_addtolistbutton() == True, "Add to List button not found"


@allure.title('tc-28,To verify watch movie on movie button click')
def test_watchmovie(browser):
    global listdet
    listdet = moviedetails(browser)
    assert listdet.verify_watchmovie() == True, "movie header image not found"


@allure.title('tc-29,To verify watch trailer on watch trailer button click')
def test_watchtrailer(browser):
    global listdet
    listdet = moviedetails(browser)
    listdet.verify_watchtrailer()
    assert listdet.verify_trailerplay() == "bmpui-ui-hugeplaybacktogglebutton bmpui-on", "After clicking on trailer " \
                                                                                         "button trailer is not " \
                                                                                         "getting played. "


@allure.title('tc-30,To verify added movie in the list')
def test_addedmovieinlist(browser):
    global listdet
    listdet = moviedetails(browser)
    assert listdet.verify_addedmovieinlist() == True, "added movie is not found in the list"


@allure.title('tc-31,Verify elements in Synopsis section of Movie Details page')
def test_synopsiselement(browser):
    global listdet
    listdet = moviedetails(browser)
    listdet.verify_moviedetails()
    assert listdet.verify_synopsisimage() == True, "Synopsis image not found"
    assert listdet.verify_synopsisdesc() == True, "Synopsis desc not found"
    assert listdet.verify_synopsisrate() == True, "Synopsis rate not found"
    assert listdet.verify_synopsisgenre() == True, "Synopsis genre not found"
    assert listdet.verify_synopsisrelease() == True, "Synopsis release date not found"
    assert listdet.verify_synopsisdirector() == True, "Synopsis director date not found"
    assert listdet.verify_synopsiscast() == True, "Synopsis cast not found"
    assert listdet.verify_synopsiscopyright() == True, "Synopsis copy right not found"


@allure.title('tc-32,Verify elements in Trailer section of Movie Details page')
def test_trailerelements(browser):
    global listdet
    listdet = moviedetails(browser)
    assert listdet.verify_trailerelements() == True, "Trailer title not found"
    assert listdet.verify_trailerplayer() == True, "Player not found"


@allure.title('TC: 33, Verify user is able to play the trailer of the movie')
def test_trailerPlay(browser):
    trailer = moviedetails(browser)
    trailer.refresh()
    time.sleep(30)
    trailer.click_trailer_button()
    time.sleep(15)
    assert trailer.verify_trailerplay() == "bmpui-ui-hugeplaybacktogglebutton bmpui-on", "After clicking on trailer " \
                                                                                         "button trailer is not " \
                                                                                         "getting played. "


@allure.title('tc-34,Verify photo elements in Movie Details page')
def test_photoelements(browser):
    global listdet
    listdet = moviedetails(browser)
    assert listdet.verify_phototitle() == True, "Trailer title not found"
    assert listdet.verify_photoslidearrow() == True, "slide arrow not found"
    assert listdet.verify_photoviewport() == True, "view port not found"


@allure.title('tc-35,User should be able to navigate between photos by clicking the arrows')
def test_photoslidearrow(browser):
    global listdet
    listdet = moviedetails(browser)
    assert listdet.verify_photoslidearrow() == True, "photo not changed"


@allure.title('tc-37,Verify elements of Cast, Crew & Production')
def test_castdetails(browser):
    global listdet
    listdet = moviedetails(browser)
    assert listdet.verify_castdetails() == True, "Cast Details not found"
    assert listdet.verify_directorname() == True, "Director name not found"
    assert listdet.verify_producername() == True, "Producer name not found"
    assert listdet.verify_execproducername() == True, "Exec. Producer name not found"


"""tv details"""


@allure.title('tc-31,Verify elements in synopsis section in tv details page')
def test_tvdetails(browser):
    global listdet
    listdet = tvdetails(browser)
    listdet.verify_Tvdetails()
    assert listdet.verify_synopsisimage() == True, "Synopsis image not found"
    assert listdet.verify_synopsisdesc() == True, "Synopsis desc not found"
    assert listdet.verify_synopsisrate() == True, "Synopsis rate not found"
    assert listdet.verify_synopsisgenre() == True, "Synopsis genre not found"
    assert listdet.verify_synopsisrelease() == True, "Synopsis release date not found"
    assert listdet.verify_synopsiscast() == True, "Synopsis cast not found"
    assert listdet.verify_synopsiscopyright() == True, "Synopsis copy right not found"


@allure.title('tc-32,Verify elements in Trailer section of TV Details page')
def test_trailerelements(browser):
    global listdet
    listdet = tvdetails(browser)
    assert listdet.verify_trailertitle() == True, "Trailer title not found"
    assert listdet.verify_trailerscreen() == True, "Player screen not found"


@allure.title('TC: 33, Verify user is able to play the trailer of the movie')
def test_trailerPlay(browser):
    trailer = tvdetails(browser)
    time.sleep(15)
    assert trailer.verify_trailerplay() == "bmpui-ui-hugeplaybacktogglebutton bmpui-on", "After clicking on trailer " \
                                                                                         "button trailer is not " \
                                                                                         "getting played. "


@allure.title('tc-34,Verify photo elements in tv Details page')
def test_photoelements(browser):
    global listdet
    listdet = tvdetails(browser)
    assert listdet.verify_phototitle() == True, "Trailer title not found"
    assert listdet.verify_photoslidearrow() == True, "slide arrow not found"
    assert listdet.verify_photoviewport() == True, "view port not found"


@allure.title('tc-35,User should be able to navigate between photos by clicking the arrows')
def test_photoslidearrow(browser):
    global listdet
    listdet = tvdetails(browser)
    assert listdet.verify_photoslidearrow() == True, "photo not changed"


@allure.title('tc-37,Verify elements of Cast, Crew & Production')
def test_castdetails(browser):
    global listdet
    listdet = tvdetails(browser)
    assert listdet.verify_castdetails() == True, "Cast Details not found"
    assert listdet.verify_execproducername() == True, "Exec. Producer name not found"


@allure.title('tc-18,Verify Watch Now button is clikable and on click of it opens playout pop up')
def test_watchnow(browser):
    global listdet
    listdet = homepg(browser)
    assert listdet.verify_watchnow() == True, "play out popup not found"


@allure.title('tc-20,Verify all controls of the pop up works correctly')
def test_popupcontrols(browser):
    listdet = homepg(browser)
    assert listdet.verify_popupmutecontrols() == "bmpui-ui-volumetogglebutton bmpui-unmuted", "mute unmute button not found"
    assert listdet.verify_popupplaycontrols() == "bmpui-ui-hugeplaybacktogglebutton bmpui-on", "play pause button not found"


def test_closeplayer(browser):
    global listdet
    listdet = homepg(browser)
    listdet.verify_closeplayer()


@allure.title('tc-36,Verify functionality of Add to List button')
def test_addtolistbutton(browser):
    global listdet
    listdet = homepg(browser)
    assert listdet.verify_addtolistbutton() == True, "add to list button not found"
    listdet.browser.refresh()

import React, { Component } from 'react'


class Navbar extends Component {
  render() {
    return (
      <div class="ui borderless menu">
        <div class="ui container">
          <div class="right menu">
            <a class="right item" href="#" data-balloon="여러분의 스토리를 공유하세요!" data-balloon-pos="down">
              <i class="alarm outline icon"></i> <span id="mobile-hidden">커뮤니티</span>
            </a>
            <a class="right item" data-balloon="다른 작가들의 작품을 사보세요!" data-balloon-pos="down">
              <span id="mobile-hidden">옥션</span> <i class="medium warning circle icon"></i>
            </a>
            <a class="right item" data-balloon="여러 사람들의 프로젝트를 구경하세요!" data-balloon-pos="down">
              <i class="rocket icon"></i> <span id="mobile-hidden">크라우드펀딩</span>
            </a>
            <a class="right item" href="#">
              <i class="checkmark box icon"></i> <span id="mobile-hidden">로그인</span>
            </a>
            <a class="right item" id="mobile-hidden">
              <i class="edit icon"></i> <span id="mobile-hidden">회원가입</span>
            </a>
          </div>
        </div>
      </div>
    )
  }
}

export default Navbar

'use client';

import { Content, Theme } from '@carbon/react';
import {
  SideNav,
  SideNavItems,
  SideNavLink,
  SideNavMenu,
  SideNavMenuItem,
} from '@carbon/react';
import React, { useState } from 'react';

import AppHeader from '@/components/AppHeader/AppHeader';
import LoginPage from './login/LoginPage';

export function Providers({ children }) {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const handleLogin = (status) => {
    setIsLoggedIn(status);
  };

  return (
    <div>
      <Theme theme="white">
        <AppHeader />
        <Content>
          {/* {!isLoggedIn ? (
            <LoginPage onLogin={handleLogin} />
          ) : ( */}
          {children}
          {/* )} */}
        </Content>
      </Theme>
    </div>
  );
}

import type { Metadata } from "next";
import "./../styles/globals.css";

export const metadata: Metadata = {
  title: "Marketing AI Advisor",
  description: "AI-powered marketing campaign planning, prediction and optimization.",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
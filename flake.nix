{
  description = "Python PyQt6 file browser environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
    in {
      devShells.${system}.default = pkgs.mkShell {
        packages = with pkgs; [
          python3
          pyright
          ruff
          python3Packages.python-lsp-server
          python3Packages.pyqt6
          python3Packages.pyqt6-webengine
          qt6.qtbase
          qt6.qttools
          qt6.qtwebengine
          qt6.qtsvg
          qt6.qtwayland
          pkg-config
          glib
        ];

        env = {
          QT_QPA_PLATFORM = "wayland;xcb";
        };
      };
    };
}
